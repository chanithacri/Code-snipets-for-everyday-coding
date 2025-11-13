/**
 * Test for fetch_get_post: Fetch GET/POST requests
 * TODO: Implement actual Jest/Mocha tests.
 */
const { getJson, postJson, request, FetchRequestError } = require("../../javascript/fetch_get_post.js");

test("fetch_get_post exports", () => {
    expect(typeof getJson).toBe("function");
    expect(typeof postJson).toBe("function");
    expect(typeof request).toBe("function");
    expect(typeof FetchRequestError).toBe("function");
});
