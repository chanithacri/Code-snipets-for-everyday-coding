# Integration Standards (Framework-Agnostic)

**Goal:** Any snippet should drop into any project with only small adjustments.

## Principles
1. **Pure Core + Thin I/O**: Keep business logic pure; isolate filesystem, network, and DB.
2. **Config Injection**: Accept config via function args or env vars (`CONFIG_*`), not globals.
3. **Dependency Inversion**: Depend on small interfaces (e.g., `Logger`, `HttpClient`).
4. **No Heavy Frameworks**: Use stdlib first; optional deps behind feature flags.
5. **Predictable Errors**: Throw/return typed errors or result objects with clear codes.
6. **Return Plain Data**: Dicts/POJOs/records, no framework objects.
7. **Logging**: Accept an optional logger; default to no-op.
8. **Versioning**: Semantic Versioning for breaking changes.
9. **Testing**: Provide unit tests independent of frameworks.
10. **Docs**: Each snippet must have header comments and a short usage example.

## Minimal Config Conventions
- `.env` keys prefixed with `APP_` or `SNIPPET_`
- `config/config.json` overrides env if present
