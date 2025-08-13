# Repository Guidelines

## Project Structure & Module Organization
- `src/py_eveng/`: core library, CLI (`cli/`), plugins, schemas, templates.
- `src/tests/`: pytest suites (`api/`, `cli/`, `data/`).
- `examples/`: sample topologies, templates, configs used by the CLI.
- `docs/` + `mkdocs.yml`: MkDocs documentation site.
- Supporting files: `Makefile`, `tox.ini`, `pytest.ini`, `.pre-commit-config.yaml`.

## Build, Test, and Development Commands
- `make lint`: run pre-commit hooks (Black, flake8, etc.).
- `make test`: run pytest against `src/tests`.
- `make coverage`: run tests with coverage and open HTML report in `htmlcov/`.
- `tox`: run matrix tests (uses envs in `tox.ini`).
- `make dist`: build sdist/wheel under `dist/`.
- `make install`: install the package locally.
- `mkdocs serve`: preview docs locally; `make docs` deploys to GitHub Pages.

## Coding Style & Naming Conventions
- Indentation: 4 spaces (`.editorconfig`). Max line length: 120 (`.flake8`).
- Formatting: Black via pre-commit; run `make lint` before committing.
- Naming: modules/functions `snake_case`, classes `PascalCase`, constants `UPPER_CASE`.
- Imports: prefer absolute imports within `py_eveng`.

## Testing Guidelines
- Framework: pytest; tests live in `src/tests` and should follow `test_*.py` naming.
- Marks: use `@pytest.mark.slow` where appropriate (see `pytest.ini`).
- Run: `make test` for quick runs, `tox` for full matrix, `make coverage` for reports.
- Data: place fixtures/test assets under `src/tests/data/`.

## Commit & Pull Request Guidelines
- Commits: use concise, imperative subjects; prefix with Jira key when applicable (e.g., `OMS-1234 Fix login flow`). Use `[skip ci]` only for doc-only/admin changes.
- Branching/PRs: target `dev` unless otherwise agreed. Fill out `.github/pull_request_template.md` including linked Jira issue, testing notes, checklist, and screenshots when UI/CLI output is relevant.
- Keep PRs focused and small; include tests and docs updates.

## Security & Configuration Tips
- Do not commit secrets. Configure EVE‑NG via environment variables (e.g., `EVE_NG_HOST`, `EVE_NG_USERNAME`, `EVE_NG_PASSWORD`, `EVE_NG_PROTOCOL`).
- When running the CLI, export vars or use a local `.env` file loaded by `python-dotenv`.
- Example: `eve-ng lab create-from-topology -t examples/test_topology.yml --template-dir examples/templates`.

