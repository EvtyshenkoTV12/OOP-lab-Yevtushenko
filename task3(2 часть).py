class Consumer:
    def __init__(self, name, surname, patronymic, phone_number):
        self.surname = surname
        self.name = name
        self._patronymic = patronymic
        self.phone_number = phone_number

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def patronymic(self):
        return self._patronymic

    @property
    def phone_number(self):
        return self._phone_number

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str):
            raise Exception("Given name is not a string")
        self._name = new_name

    @surname.setter
    def surname(self, new_surname):
        if not isinstance(new_surname, str):
            raise Exception("Given surname is not a string")
        self._surname = new_surname

    @phone_number.setter
    def phone_number(self, new_phone_num):
        if not isinstance(new_phone_num, str):
            raise Exception("Given phone number is not a string")
        self._phone_number = new_phone_num

    def __str__(self):
        return f"Personal info: {self.surname} {self.name} {self.patronymic}\n" \
               f"Phone number: {self.phone_number}"


class Product:
    def __init__(self, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions

    @property
    def price(self):
        return self._price

    @property
    def description(self):
        return self._description

    @property
    def dimensions(self):
        return self._dimensions

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise Exception("Given price isn't a float value")
        self._price = new_price

    @description.setter
    def description(self, new_description):
        if not isinstance(new_description, str):
            raise Exception("Given description isn't a string")
        self._description = new_description

    @dimensions.setter
    def dimensions(self, new_dimensions):
        if not isinstance(new_dimensions, list) and not isinstance(new_dimensions, tuple):
            raise Exception("Given dimensions aren't a string or tuple")
        if not len(new_dimensions) == 3:
            raise Exception("Given not 3 dimensions")
        for dimension in new_dimensions:
            if not isinstance(dimension, float) and not isinstance(dimension, int):
                raise Exception("Given dimensions aren't float or integer values")
        self._dimensions = tuple(new_dimensions)

    def __str__(self):
        return f"Product '{self.description}' costs {self.price} hrn and its dimensions: {self.dimensions} cm"


class Order:
    def __init__(self, consumer):
        if not isinstance(consumer, Consumer):
            raise Exception("Consumer parameter is not of the type 'Consumer'")
        self._consumer = consumer
        self._products = []

    @property
    def consumer(self):
        return self._consumer

    def add_product(self, product):
        if len(self._products) >= 10:
            raise Exception("Added more than 10 products")
        if not isinstance(product, Product):
            raise Exception("Given parameter isn't of type 'Product'")
        self._products.append(product)

    def remove_product(self, product_name):
        if not isinstance(product_name, str):
            raise Exception("Given product name is not a string")
        for product in self._products:
            if product.description == product_name:
                self._products.remove(product)

    def __str__(self):
        result = f"Order of:\n{self.consumer}:\n"
        result += "\n".join(map(str, self._products))
        total_price = 0
        for product in self._products:
            total_price += product.price
        result += f"\nTotal price: {total_price} hrn"
        return result
