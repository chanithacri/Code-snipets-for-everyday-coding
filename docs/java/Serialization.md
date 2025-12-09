# Serialization

**Language:** Java

## Overview
* Serialization: Serialize/deserialize objects.

## Usage
```java
// Compile and run
// javac java/Serialization.java
// java Serialization
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/java/SerializationTest.java

_Generated: 2025-12-08T17:27:58.299843Z_
