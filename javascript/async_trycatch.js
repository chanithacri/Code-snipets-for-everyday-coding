/**
 * async_trycatch: Async/await with try/catch patterns.
 * Include minimal usage example at bottom.
 */

export async function safeFetch(fetchImpl, url, options = {}) {
  if (typeof fetchImpl !== "function") {
    throw new Error("A fetch implementation is required");
  }
  try {
    const response = await fetchImpl(url, options);
    const data = await response.json().catch(() => null);
    return { ok: true, response, data };
  } catch (error) {
    return { ok: false, error };
  }
}

export async function withRetry(task, retries = 1, delayMs = 50) {
  let attempt = 0;
  while (attempt <= retries) {
    try {
      return await task();
    } catch (error) {
      if (attempt === retries) {
        throw error;
      }
      await new Promise((resolve) => setTimeout(resolve, delayMs));
      attempt += 1;
    }
  }
  throw new Error("Retry attempts exhausted");
}

/* Usage example:
import fetch from "node-fetch";

const { ok, data, error } = await safeFetch(fetch, "https://httpbin.org/json");
const result = await withRetry(() => safeFetch(fetch, "https://httpbin.org/status/200"), 2);
*/
