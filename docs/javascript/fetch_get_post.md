# fetch_get_post

**Language:** Javascript

## Overview
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

## Usage
```javascript
# TODO: add example
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/javascript/fetch_get_post.test.js

_Generated: 2025-11-13T13:55:58.559845Z_
