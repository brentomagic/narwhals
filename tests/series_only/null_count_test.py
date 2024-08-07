from __future__ import annotations

from typing import Any

import narwhals as nw


def test_null_count(constructor_series: Any) -> None:
    data = [1, 2, None]
    series = nw.from_native(constructor_series(data), series_only=True)
    result = series.null_count()
    assert result == 1
