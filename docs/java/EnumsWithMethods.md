# EnumsWithMethods

**Language:** Java

## Overview
* EnumsWithMethods: Enums with fields and behavior.
 *
 * The {@link Priority} enum demonstrates how to attach metadata and helper
 * methods directly on an enum. Utility methods in this class showcase common
 * lookups and formatting.

## Usage
```java
// Compile and run
// javac java/EnumsWithMethods.java
// java EnumsWithMethods
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/java/EnumsWithMethodsTest.java

_Generated: 2025-12-08T17:27:58.306883Z_
