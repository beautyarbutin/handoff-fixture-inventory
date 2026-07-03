from dataclasses import asdict
from math import isfinite
from typing import Any

from inventory.catalog import filter_items
from inventory.models import SAMPLE_ITEMS, Item


def _price_value(query: dict[str, Any], key: str) -> float | None:
    if key not in query or query[key] is None:
        return None

    value = query[key]
    if isinstance(value, bool):
        raise ValueError(f"{key} must be numeric")

    try:
        price = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{key} must be numeric") from exc

    if not isfinite(price):
        raise ValueError(f"{key} must be numeric")

    return price


def search_items(query: dict[str, Any], items: list[Item] | None = None) -> list[dict[str, Any]]:
    """Search inventory items for API clients.

    Reuses catalog filtering and returns plain dictionaries for API clients.
    """
    catalog_items = SAMPLE_ITEMS if items is None else items
    filtered_items = filter_items(
        catalog_items,
        category=query.get("category"),
        min_price=_price_value(query, "min_price"),
        max_price=_price_value(query, "max_price"),
        in_stock=query.get("in_stock"),
    )

    return [asdict(item) for item in filtered_items]

