/**
 * Test for jwt_flow: JWT authentication flow
 * TODO: Implement actual Jest/Mocha tests.
 */
const { createJwt, verifyJwt, decodeJwt } = require("../../javascript/jwt_flow.js");

test("jwt_flow exports", () => {
    expect(typeof createJwt).toBe("function");
    expect(typeof verifyJwt).toBe("function");
    expect(typeof decodeJwt).toBe("function");
});
