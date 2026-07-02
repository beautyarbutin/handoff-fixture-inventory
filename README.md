# handoff-fixture-inventory

Small fixture repository for handoff ablation experiments.

The repository is intentionally positioned after a completed predecessor task
(`T1`) and before a successor task (`T2`):

- `T1` completed the inventory filtering logic in `src/inventory/catalog.py`.
- `T2` should expose that filtering logic through `src/inventory/api.py`.

Use HALF to vary the handoff content passed to Codex before running `T2`.

## Install

```bash
python -m pip install -e ".[dev]"
```

## Current Baseline

The predecessor implementation should pass:

```bash
pytest
```

The successor contract is stored separately under `evaluation_tests/` and is
not part of the default pytest run:

```bash
pytest tests evaluation_tests
```

Before `T2` is implemented, the full evaluation test command is expected to
fail. After a successful `T2`, both commands should pass.

## Experiment

Use `docs/canonical_handoff.json` as the full handoff. Derive arms by removing
fields or converting it to a natural-language summary.

Suggested arms:

- `A_full`
- `B_no_verification`
- `C_no_unfinished_items`
- `D_no_risks`
- `E_summary_only`
- `F_full_context`

