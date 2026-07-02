from inventory.catalog import filter_items
from inventory.models import SAMPLE_ITEMS


def test_filters_category_case_insensitively():
    results = filter_items(SAMPLE_ITEMS, category="BOOKS")

    assert [item.sku for item in results] == ["BK-001", "BK-002"]


def test_price_bounds_are_inclusive():
    results = filter_items(SAMPLE_ITEMS, min_price=9.99, max_price=12.50)

    assert [item.sku for item in results] == ["BK-001", "BK-002"]


def test_filters_by_stock_status():
    results = filter_items(SAMPLE_ITEMS, category="electronics", in_stock=True)

    assert [item.sku for item in results] == ["EL-001"]

