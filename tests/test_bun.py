import pytest

from bun import Bun


class TestBun:
    @pytest.mark.parametrize(
        ("name", "price"),
        [
            ("black bun", 100.0),
            ("sesame bun", 125.5),
            ("plain bun", 0.0),
        ],
    )
    def test_get_name_returns_bun_name(self, name, price):
        bun = Bun(name, price)

        assert bun.get_name() == name

    @pytest.mark.parametrize(
        ("name", "price"),
        [
            ("black bun", 100.0),
            ("sesame bun", 125.5),
            ("plain bun", 0.0),
        ],
    )
    def test_get_price_returns_bun_price(self, name, price):
        bun = Bun(name, price)

        assert bun.get_price() == price
