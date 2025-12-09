# JsonParser

**Language:** Java

## Overview
* JsonParser: Parse JSON with Jackson/Gson.
 *
 * Provides minimal parsing for flat JSON objects without introducing external
 * dependencies. The parser expects simple string key/value pairs, making it
 * suitable for configuration-style payloads.

## Usage
```java
// Compile and run
// javac java/JsonParser.java
// java JsonParser
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/java/JsonParserTest.java

_Generated: 2025-12-08T17:27:58.302263Z_
