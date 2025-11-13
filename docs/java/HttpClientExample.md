# HttpClientExample

**Language:** Java

## Overview
* Lightweight wrapper around {@link HttpClient} for GET and POST requests.
 *
 * <p>The helpers return a {@link HttpResult} record which keeps data transport
 * friendly for further processing. Logging is optional and defaults to a
 * no-op consumer.</p>
 *
 * <h2>Usage example</h2>
 * <pre>{@code
 * HttpClientExample.HttpResult result = HttpClientExample.get("https://example.test/api");
 * System.out.println(result.statusCode());
 * System.out.println(result.body());
 * }
 * </pre>

## Usage
```java
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
See: tests/java/HttpClientExampleTest.java

_Generated: 2025-11-13T13:55:58.556819Z_
