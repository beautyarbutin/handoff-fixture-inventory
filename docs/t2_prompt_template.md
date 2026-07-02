# T2 Prompt Template

You are working in the `handoff-fixture-inventory` repository.

Use only the handoff block provided below as predecessor context. Do not infer
predecessor facts that are not present in the handoff. If important context is
missing, complete the task using visible repository code and mention the missing
context in your final report.

## Handoff

{{HANDOFF_BLOCK}}

## Successor Task

Expose the predecessor filtering logic through `src/inventory/api.py`.

Requirements:

1. Implement `search_items(query, items=None)`.
2. Reuse `inventory.catalog.filter_items`; do not copy the filtering algorithm
   into `api.py`.
3. Support `category`, `min_price`, `max_price`, and `in_stock` query keys.
4. Ignore unknown query keys.
5. Reject non-numeric `min_price` and `max_price` values with `ValueError`.
6. Return a list of plain dictionaries with `sku`, `name`, `category`, `price`,
   and `in_stock`.
7. Keep the existing catalog tests passing.

Run:

```bash
pytest tests evaluation_tests
```

Report the commands run and the result.

