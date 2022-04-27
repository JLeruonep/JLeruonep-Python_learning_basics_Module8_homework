class Product:
    def __init__(self, title='', calorific=1, cost=1):
        self._title = title
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

    @property
    def calorific(self):
        return self._calorific

    @calorific.setter
    def calorific(self, value):
        if value > 0:
            self._calorific = value
        else:
            raise ValueError('Значение не может быть меньше нуля или равно нулю')

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if value > 0:
            self._cost = value
        else:
            raise ValueError('Значение не может быть меньше нуля или равно нулю')


class Ingredient:
    def __init__(self, product, weight):
        if weight > 0:
            self.product = product
            self._weight = weight
        else:
            raise ValueError('Значение веса должно быть положительным')

    def get_calorific(self):
        return self._weight / 100 * self.product.calorific  # product calorific?

    def get_cost(self):
        return self._weight / 100 * self.product.cost  # product cost?

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self._weight = value
        else:
            raise ValueError('Значение веса должно быть положительным')


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
