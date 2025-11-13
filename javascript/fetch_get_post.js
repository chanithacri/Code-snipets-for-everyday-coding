/**
 * Fetch API helpers for GET and POST requests.
 *
 * The module keeps the core HTTP logic pure. Callers may supply a custom
 * `fetchImpl` (for example from `node-fetch`) which makes the helpers easy to
 * unit test or reuse in environments without a global `fetch`.
 *
 * Usage example:
 * ```js
 * const { getJson, postJson } = require("./fetch_get_post.js");
 *
 * const list = await getJson("https://example.test/api/items");
 * await postJson("https://example.test/api/items", { name: "demo" });
 * ```
 */
const defaultFetch = typeof fetch === "function" ? (...args) => fetch(...args) : null;

/**
 * Error thrown when a request fails before producing a response.
 */
class FetchRequestError extends Error {
  constructor(message, options) {
    super(message, options);
    this.name = "FetchRequestError";
  }
}

const NO_OP_LOGGER = () => {};

function asPlainHeaders(headers) {
  const result = {};
  if (!headers) {
    return result;
  }
  for (const [key, value] of headers.entries()) {
    result[key.toLowerCase()] = value;
  }
  return result;
}

function normaliseBody(body, headers) {
  if (body == null) {
    return { payload: undefined, headers };
  }
  if (typeof body === "string" || body instanceof ArrayBuffer || body instanceof Blob) {
    return { payload: body, headers };
  }
  if (body instanceof FormData || body instanceof URLSearchParams) {
    return { payload: body, headers };
  }
  if (!headers.has("content-type")) {
    headers.set("content-type", "application/json");
  }
  return { payload: JSON.stringify(body), headers };
}

async function parseBody(response) {
  const contentType = response.headers.get("content-type") || "";
  if (contentType.includes("application/json")) {
    try {
      return await response.json();
    } catch (error) {
      return undefined;
    }
  }
  if (contentType.startsWith("text/")) {
    return await response.text();
  }
  return await response.arrayBuffer();
}

/**
 * Perform an HTTP request using Fetch.
 * @param {string} method
 * @param {string} url
 * @param {object} [options]
 * @param {any} [options.body]
 * @param {HeadersInit} [options.headers]
 * @param {AbortSignal} [options.signal]
 * @param {function(string):void} [options.logger]
 * @param {function} [options.fetchImpl]
 * @returns {Promise<{ok: boolean, status: number, headers: object, data: any}>}
 */
async function request(method, url, options = {}) {
  const {
    body,
    headers: initialHeaders = {},
    signal,
    logger = NO_OP_LOGGER,
    fetchImpl = defaultFetch,
  } = options;

  if (typeof fetchImpl !== "function") {
    throw new FetchRequestError("A fetch implementation must be provided.");
  }

  const headers = new Headers(initialHeaders);
  const { payload, headers: finalHeaders } = normaliseBody(body, headers);

  try {
    logger(`fetch: ${method.toUpperCase()} ${url}`);
    const response = await fetchImpl(url, {
      method,
      headers: finalHeaders,
      body: payload,
      signal,
    });
    const data = await parseBody(response);
    return {
      ok: response.ok,
      status: response.status,
      headers: asPlainHeaders(response.headers),
      data,
    };
  } catch (error) {
    logger(`fetch: request to ${url} failed: ${error}`);
    throw new FetchRequestError(`Request to ${url} failed`, { cause: error });
  }
}

function getJson(url, options = {}) {
  return request("GET", url, options);
}

function postJson(url, body, options = {}) {
  return request("POST", url, { ...options, body });
}

module.exports = {
  FetchRequestError,
  request,
  getJson,
  postJson,
};
