/**
 * Test for jwt_flow: JWT authentication flow
 * Validate JWT creation and verification flows.
 */
const { createJwt, verifyJwt, decodeJwt } = require("../../javascript/jwt_flow.js");

describe("jwt_flow", () => {
    test("creates and verifies a token", () => {
        const token = createJwt({ sub: "abc" }, "secret", { expiresInSeconds: 30 });
        const { valid, payload } = verifyJwt(token, "secret");
        expect(valid).toBe(true);
        expect(payload.sub).toBe("abc");
    });

    test("fails verification with wrong secret", () => {
        const token = createJwt({ role: "user" }, "secret");
        const result = verifyJwt(token, "bad-secret");
        expect(result.valid).toBe(false);
        expect(result.reason).toBe("invalid_signature");
    });

    test("decode rejects malformed tokens", () => {
        expect(decodeJwt("not-a-token")).toBeNull();
    });
});
