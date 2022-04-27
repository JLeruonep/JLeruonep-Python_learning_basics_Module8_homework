class TitleChecker:
    '''
    Класс используется как базовый для проверки тайтла
    '''
    def __init__(self, title):
        if title == '':
            raise ValueError('Название не может быть пустым')
        else:
            self.title = title

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value == '':
            raise ValueError('Название не может быть пустым')
        else:
            self.__title = value


class Product(TitleChecker):
    def __init__(self, title, calorific, cost):
        super().__init__(title)
        self.__title = title
        self.calorific = calorific
        self.cost = cost

    @property
    def calorific(self):
        return self.__calorific

    @calorific.setter
    def calorific(self, value):
        if value > 0:
            self.__calorific = value
        else:
            raise ValueError('Значение не может быть меньше нуля или равно нулю')

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        if value > 0:
            self.__cost = value
        else:
            raise ValueError('Значение не может быть меньше нуля или равно нулю')


class Ingredient:
    def __init__(self, product, weight):
        if weight > 0:
            self.product = product
            self.__weight = weight
        else:
            raise ValueError('Значение веса должно быть положительным')

    def get_calorific(self):
        return self.__weight / 100 * self.product.calorific  # product calorific?

    def get_cost(self):
        return self.__weight / 100 * self.product.cost  # product cost?

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        if value > 0:
            self.__weight = value
        else:
            raise ValueError('Значение веса должно быть положительным')


class Pizza(TitleChecker):
    def __init__(self, title, ingredients):
        super().__init__(title)
        self.title = title
        self.ingredients = ingredients

    def __str__(self):
        return f'{self.title} ({self.get_calorific()} kcal) - {self.get_cost()} руб'

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
