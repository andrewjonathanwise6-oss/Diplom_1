from database import Database
from ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


class TestDatabase:
    def test_database_initializes_buns(self):
        database = Database()

        actual = [(bun.get_name(), bun.get_price()) for bun in database.buns]

        assert actual == [
            ("black bun", 100),
            ("white bun", 200),
            ("red bun", 300),
        ]

    def test_database_initializes_ingredients(self):
        database = Database()

        actual = [
            (ingredient.get_type(), ingredient.get_name(), ingredient.get_price())
            for ingredient in database.ingredients
        ]

        assert actual == [
            (INGREDIENT_TYPE_SAUCE, "hot sauce", 100),
            (INGREDIENT_TYPE_SAUCE, "sour cream", 200),
            (INGREDIENT_TYPE_SAUCE, "chili sauce", 300),
            (INGREDIENT_TYPE_FILLING, "cutlet", 100),
            (INGREDIENT_TYPE_FILLING, "dinosaur", 200),
            (INGREDIENT_TYPE_FILLING, "sausage", 300),
        ]

    def test_available_buns_returns_database_bun_list(self):
        database = Database()

        assert database.available_buns() is database.buns

    def test_available_ingredients_returns_database_ingredient_list(self):
        database = Database()

        assert database.available_ingredients() is database.ingredients
