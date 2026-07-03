from numbers import Real
from typing import Any

from inventory import catalog
from inventory.models import SAMPLE_ITEMS, Item


def _numeric_query_value(query: dict[str, Any], key: str) -> float | None:
    value = query.get(key)
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, Real):
        raise ValueError(f"{key} must be numeric")
    return float(value)


def search_items(query: dict[str, Any], items: list[Item] | None = None) -> list[dict[str, Any]]:
    """Search inventory items for API clients.

    Unknown query keys are ignored.
    """
    filtered_items = catalog.filter_items(
        SAMPLE_ITEMS if items is None else items,
        category=query.get("category"),
        min_price=_numeric_query_value(query, "min_price"),
        max_price=_numeric_query_value(query, "max_price"),
        in_stock=query.get("in_stock"),
    )

    return [
        {
            "sku": item.sku,
            "name": item.name,
            "category": item.category,
            "price": item.price,
            "in_stock": item.in_stock,
        }
        for item in filtered_items
    ]

