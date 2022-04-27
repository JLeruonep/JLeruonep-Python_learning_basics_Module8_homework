class Product:
    def __init__(self, title='', calorific=0, cost=0):
        if title == '':
            raise ValueError('Название не может быть пустым')
        else:
            self._title = title
        if calorific <= 0 or cost <= 0:
            raise ValueError('Значения не могут быть меньше нуля')
        else:
            self.calorific = calorific
            self.cost = cost

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
        if weight <= 0:
            raise ValueError('Значение веса не может быть меньше нуля')
        else:
            self.product = product
            self.weight = weight

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
