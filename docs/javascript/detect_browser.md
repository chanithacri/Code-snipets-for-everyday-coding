# detect_browser

**Language:** Javascript

## Overview
* detect_browser: Detect browser/device basics.
 * Include minimal usage example at bottom.

## Usage
```javascript
import * as mod from './javascript/detect_browser.js';
// Call the exported helpers, e.g. mod.example();
```

## Integration Notes
- Accept config via function args/env variables
- Avoid global state and singletons
- Provide small adapter layers for logging and HTTP
- Return plain data structures (dicts/POJOs) not framework-specific objects

## Dependencies
- Keep optional and small. Avoid heavy frameworks.

## Tests
See: tests/javascript/detect_browser.test.js

_Generated: 2025-12-08T17:27:58.319755Z_
