# Universal Code Snippets — Combined (Phases 1–3)

This repository merges:
- **Phase 1:** Full snippet scaffold with manifest
- **Phase 2:** Tests + tasks.json + CI (multi-language)
- **Phase 3:** Docs generator + progress tracker + integration standards & adapters

## Quickstart
1. Browse `manifest.json` to see all stubs.
2. Use your Codex/agent to iterate `tasks.json` and implement snippets.
3. Run docs generator:
   ```bash
   python scripts/generate_docs.py
   ```

## CI
- `.github/workflows/codex_test.yml` – runs language smoke tests
- `.github/workflows/docs.yml` – generates docs & updates progress

## Integration
All snippets adhere to the standards in `standards/INTEGRATION_STANDARDS.md` and can be dropped into any project with minimal edits. Adapters in `adapters/` provide no-op logging and env-based config.
