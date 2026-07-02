Predecessor task T1 completed the inventory filtering core.

Files touched:

- `src/inventory/models.py`
- `src/inventory/catalog.py`
- `tests/test_catalog.py`

The repository now contains an immutable `Item` model, a small `SAMPLE_ITEMS`
fixture, and `filter_items(items, category=None, min_price=None,
max_price=None, in_stock=None)`.

Important implementation details from T1:

- Category filtering compares values case-insensitively with `casefold()`.
- `min_price` and `max_price` are inclusive.
- `in_stock` filters by exact boolean status.
- The function returns the original `Item` objects in input order.

Tests added in T1:

- `test_filters_category_case_insensitively`
- `test_price_bounds_are_inclusive`
- `test_filters_by_stock_status`

T1 verification:

```text
pytest
3 passed
```

Remaining work:

- `src/inventory/api.py` still raises `NotImplementedError`.
- API callers need plain dictionaries instead of `Item` objects.
- API-level combinations are not covered yet.

Constraints:

- Do not duplicate the filtering algorithm in `api.py`.
- Reuse `inventory.catalog.filter_items`.
- Unknown query keys should be ignored.
- Invalid numeric query values should fail clearly.

