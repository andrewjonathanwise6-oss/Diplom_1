import pytest

from bun import Bun


@pytest.mark.parametrize(
    ("name", "price"),
    [
        ("black bun", 100.0),
        ("sesame bun", 125.5),
        ("plain bun", 0.0),
    ],
)
def test_bun_returns_its_name_and_price(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price
