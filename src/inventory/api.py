from dataclasses import asdict
from math import isfinite
from typing import Any

from inventory.catalog import filter_items
from inventory.models import SAMPLE_ITEMS, Item


def _price_query_value(query: dict[str, Any], key: str) -> float | None:
    if key not in query or query[key] is None:
        return None

    if isinstance(query[key], bool):
        raise ValueError(f"{key} must be numeric")

    try:
        value = float(query[key])
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{key} must be numeric") from exc

    if not isfinite(value):
        raise ValueError(f"{key} must be finite")

    return value


def _category_query_value(query: dict[str, Any]) -> str | None:
    value = query.get("category")
    return None if value is None else str(value)


def _in_stock_query_value(query: dict[str, Any]) -> bool | None:
    if "in_stock" not in query or query["in_stock"] is None:
        return None

    value = query["in_stock"]
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().casefold()
        if normalized in {"true", "1", "yes"}:
            return True
        if normalized in {"false", "0", "no"}:
            return False

    return None


def search_items(query: dict[str, Any], items: list[Item] | None = None) -> list[dict[str, Any]]:
    """Search inventory items for API clients.

    Unknown query keys are ignored.
    """
    filtered_items = filter_items(
        SAMPLE_ITEMS if items is None else items,
        category=_category_query_value(query),
        min_price=_price_query_value(query, "min_price"),
        max_price=_price_query_value(query, "max_price"),
        in_stock=_in_stock_query_value(query),
    )

    return [asdict(item) for item in filtered_items]

