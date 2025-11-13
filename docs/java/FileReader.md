# FileReader

**Language:** Java

## Overview
* Utility helpers for reading and writing files.
 *
 * <p>The helpers keep business logic isolated from I/O, wrap checked exceptions
 * into {@link FileAccessException}, and accept an optional logger so callers can
 * integrate with their observability stack.</p>
 *
 * <h2>Usage example</h2>
 * <pre>{@code
 * Path file = Path.of("example.txt");
 * FileReader.writeText(file, "hello world");
 * String contents = FileReader.readText(file);
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
See: tests/java/FileReaderTest.java

_Generated: 2025-11-13T17:21:27.104754Z_
