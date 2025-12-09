# ApachePOIExcel

**Language:** Java

## Overview
* ApachePOIExcel: Read/write Excel with Apache POI.
 *
 * The helper methods avoid a hard dependency on Apache POI while still showing
 * how data could be structured for export. The returned data maps sheet names
 * to row/column values that can be fed into a workbook builder in a project
 * that includes POI.

## Usage
```java
// Compile and run
// javac java/ApachePOIExcel.java
// java ApachePOIExcel
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/java/ApachePOIExcelTest.java

_Generated: 2025-12-08T17:27:58.308902Z_
