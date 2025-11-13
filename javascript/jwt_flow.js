/**
 * Minimal JWT creation and verification utilities.
 *
 * The helpers support the HS256 algorithm and avoid external dependencies. They
 * return plain JavaScript objects so the data can be reused in any runtime.
 *
 * Usage example:
 * ```js
 * const { createJwt, verifyJwt } = require("./jwt_flow.js");
 * const token = createJwt({ sub: "123" }, "secret", { expiresInSeconds: 60 });
 * const result = verifyJwt(token, "secret");
 * if (result.valid) {
 *   console.log(result.payload.sub);
 * }
 * ```
 */
const crypto = require("crypto");

const DEFAULT_HEADER = { alg: "HS256", typ: "JWT" };

function base64UrlEncode(value) {
  return Buffer.from(value)
    .toString("base64")
    .replace(/=/g, "")
    .replace(/\+/g, "-")
    .replace(/\//g, "_");
}

function base64UrlDecode(value) {
  const padLength = (4 - (value.length % 4 || 4)) % 4;
  const padded = value + "=".repeat(padLength);
  const normalised = padded.replace(/-/g, "+").replace(/_/g, "/");
  return Buffer.from(normalised, "base64");
}

function encodeSegment(segment) {
  return base64UrlEncode(JSON.stringify(segment));
}

function decodeSegment(segment) {
  try {
    return JSON.parse(base64UrlDecode(segment).toString("utf8"));
  } catch (error) {
    return null;
  }
}

function sign(data, secret) {
  return crypto.createHmac("sha256", secret).update(data).digest("base64")
    .replace(/=/g, "")
    .replace(/\+/g, "-")
    .replace(/\//g, "_");
}

function nowSeconds() {
  return Math.floor(Date.now() / 1000);
}

function createJwt(payload, secret, options = {}) {
  if (typeof payload !== "object" || payload == null) {
    throw new TypeError("payload must be an object");
  }
  if (typeof secret !== "string" || !secret) {
    throw new TypeError("secret must be a non-empty string");
  }
  const header = { ...DEFAULT_HEADER, ...(options.header || {}) };
  const issuedAt = options.issuedAt ?? nowSeconds();
  const body = { ...payload };
  if (!Object.prototype.hasOwnProperty.call(body, "iat")) {
    body.iat = issuedAt;
  }
  if (options.expiresInSeconds) {
    body.exp = issuedAt + options.expiresInSeconds;
  }
  if (options.notBeforeSeconds) {
    body.nbf = issuedAt + options.notBeforeSeconds;
  }
  const tokenWithoutSignature = `${encodeSegment(header)}.${encodeSegment(body)}`;
  const signature = sign(tokenWithoutSignature, secret);
  return `${tokenWithoutSignature}.${signature}`;
}

function decodeJwt(token) {
  if (typeof token !== "string") {
    return null;
  }
  const parts = token.split(".");
  if (parts.length !== 3) {
    return null;
  }
  const [headerSegment, payloadSegment] = parts;
  const header = decodeSegment(headerSegment);
  const payload = decodeSegment(payloadSegment);
  if (!header || !payload) {
    return null;
  }
  return { header, payload };
}

function isExpired(payload, clockToleranceSeconds, now = nowSeconds()) {
  if (typeof payload.exp === "number" && now > payload.exp + clockToleranceSeconds) {
    return true;
  }
  if (typeof payload.nbf === "number" && now + clockToleranceSeconds < payload.nbf) {
    return true;
  }
  return false;
}

function verifyJwt(token, secret, options = {}) {
  const decoded = decodeJwt(token);
  if (!decoded) {
    return { valid: false, reason: "malformed" };
  }
  const { header, payload } = decoded;
  if (header.alg !== "HS256") {
    return { valid: false, reason: "unsupported_alg", header, payload };
  }
  const tokenWithoutSignature = token.split(".").slice(0, 2).join(".");
  const expectedSignature = sign(tokenWithoutSignature, secret);
  const signature = token.split(".")[2];
  if (signature.length !== expectedSignature.length) {
    return { valid: false, reason: "invalid_signature", header, payload };
  }
  if (!crypto.timingSafeEqual(Buffer.from(signature, "utf8"), Buffer.from(expectedSignature, "utf8"))) {
    return { valid: false, reason: "invalid_signature", header, payload };
  }
  const tolerance = options.clockToleranceSeconds ?? 0;
  if (isExpired(payload, tolerance, options.nowSeconds ?? nowSeconds())) {
    return { valid: false, reason: "token_expired", header, payload };
  }
  return { valid: true, header, payload };
}

module.exports = {
  createJwt,
  verifyJwt,
  decodeJwt,
  base64UrlEncode,
  base64UrlDecode,
};
