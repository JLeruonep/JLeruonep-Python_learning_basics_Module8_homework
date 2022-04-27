class Product:
    def __init__(self, title, calorific=1, cost=1):
        if title == '':
            raise ValueError('Название не может быть пустым')
        else:
            self._title = title
        if calorific > 0 or cost > 0:
            self.calorific = calorific
            self.cost = cost
        else:
            raise ValueError('Значения не могут быть меньше нуля или равно нулю')

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Название не может быть пустым')
        else:
            self._title = value


class Ingredient:
    def __init__(self, product, weight):
        if weight > 0:
            self.product = product
            self.weight = weight
        else:
            raise ValueError('Значение веса должно быть положительным')

    def get_calorific(self):
        return self.weight / 100 * self.product.calorific  # product calorific?

    def get_cost(self):
        return self.weight / 100 * self.product.cost  # product cost?


class Pizza(Product):
    def __init__(self, title, ingredients):
        super().__init__(title)
        self._title = title
        self.ingredients = ingredients

    def __str__(self):
        return f'{self._title} ({self.get_calorific()} kcal) - {self.get_cost()} руб'

    def get_calorific(self):
        result_calories = 0
        for ingredient in self.ingredients:
            result_calories += ingredient.get_calorific()
        return result_calories

    def get_cost(self):
        result_cost = 0
        for ingredient in self.ingredients:
            result_cost += ingredient.get_cost()
        return result_cost


# Создаем продукты с указанием названия, калорийности продукта и его себестоимости
dough_product = Product('Тесто', 200, 20)
tomato_product = Product('Помидор', 100, 50)
cheese_product = Product('Сыр', 100, 120)

# Из продуктов создаем ингредиенты.
# Для каждого ингредиента указываем продукт, из которого он состоит и вес продукта
dough_ingredient = Ingredient(dough_product, 100)
tomato_ingredient = Ingredient(tomato_product, 100)
cheese_ingredient = Ingredient(cheese_product, 100)

# Из ингредиентов создаем пиццу
pizza_margarita = Pizza('Маргарита', [dough_ingredient, tomato_ingredient, cheese_ingredient])
pizza_margarita_light = Pizza('Маргарита', [dough_ingredient, cheese_ingredient])

# Выводим экземпляр пиццы

print(pizza_margarita)
print(pizza_margarita_light)
