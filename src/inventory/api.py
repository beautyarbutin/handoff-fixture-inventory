from dataclasses import asdict
from math import isfinite
from typing import Any

from inventory.catalog import filter_items
from inventory.models import SAMPLE_ITEMS, Item


def search_items(query: dict[str, Any], items: list[Item] | None = None) -> list[dict[str, Any]]:
    """Filter inventory items and return API-friendly dictionaries."""

    def price_value(name: str) -> float | None:
        value = query.get(name)
        if value is None:
            return None
        if isinstance(value, bool):
            raise ValueError(f"{name} must be numeric")
        try:
            price = float(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} must be numeric") from exc
        if not isfinite(price):
            raise ValueError(f"{name} must be numeric")
        return price

    filtered_items = filter_items(
        SAMPLE_ITEMS if items is None else items,
        category=query.get("category"),
        min_price=price_value("min_price"),
        max_price=price_value("max_price"),
        in_stock=query.get("in_stock"),
    )
    return [asdict(item) for item in filtered_items]

