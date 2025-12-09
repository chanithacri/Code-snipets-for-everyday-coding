/**
 * Test for fetch_get_post: Fetch GET/POST requests
 * Basic behavioural tests for fetch helpers.
 */
const { getJson, postJson, request, FetchRequestError } = require("../../javascript/fetch_get_post.js");

describe("fetch_get_post", () => {
    const HeadersImpl = typeof Headers !== "undefined" ? Headers : class {
        constructor(init = {}) { this.map = new Map(Object.entries(init)); }
        has(key) { return this.map.has(key.toLowerCase()); }
        set(key, value) { this.map.set(String(key).toLowerCase(), String(value)); }
        entries() { return this.map.entries(); }
        get(key) { return this.map.get(String(key).toLowerCase()) || null; }
    };

    test("returns parsed json for GET", async () => {
        const mockResponse = {
            ok: true,
            status: 200,
            headers: new HeadersImpl({ "content-type": "application/json" }),
            json: () => Promise.resolve({ hello: "world" }),
        };
        const fetchImpl = jest.fn().mockResolvedValue(mockResponse);
        const result = await getJson("https://example.test/api", { fetchImpl });
        expect(result.ok).toBe(true);
        expect(result.status).toBe(200);
        expect(result.data).toEqual({ hello: "world" });
        expect(fetchImpl).toHaveBeenCalledWith("https://example.test/api", expect.any(Object));
    });

    test("throws FetchRequestError on failure", async () => {
        const fetchImpl = jest.fn().mockRejectedValue(new Error("offline"));
        await expect(request("GET", "https://example.test", { fetchImpl })).rejects.toBeInstanceOf(FetchRequestError);
    });

    test("POST forwards body and headers", async () => {
        const headers = new HeadersImpl();
        const mockResponse = {
            ok: true,
            status: 201,
            headers: new HeadersImpl({ "content-type": "application/json" }),
            json: () => Promise.resolve({ id: 1 }),
        };
        const fetchImpl = jest.fn().mockResolvedValue(mockResponse);
        const result = await postJson("https://example.test", { name: "demo" }, { fetchImpl, headers });
        expect(result.status).toBe(201);
        expect(result.data).toEqual({ id: 1 });
        expect(fetchImpl).toHaveBeenCalledWith(
            "https://example.test",
            expect.objectContaining({ method: "POST", headers: expect.anything(), body: expect.any(String) })
        );
    });
});
