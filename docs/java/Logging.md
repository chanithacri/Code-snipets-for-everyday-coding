# Logging

**Language:** Java

## Overview
* Logging: Logging with SLF4J/Logback.
 *
 * Uses the JDK logger for a dependency-free example.

## Usage
```java
// Compile and run
// javac java/Logging.java
// java Logging
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/java/LoggingTest.java

_Generated: 2025-12-08T17:27:58.303223Z_
