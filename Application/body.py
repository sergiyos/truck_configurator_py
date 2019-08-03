
class Body:

    def __init__(self, name, typeBody, height, width, mass, price):

        self.__name = name # назва
        self.__typeBody = typeBody # тип
        self.__height = height # висота
        self.__width = width # ширина
        self.__mass = mass # маса
        self.__price = price # ціна

    def get_name(self):
        return self.__name

    def get_type_body(self):
        return self.__typeBody

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_mass(self):
        return self.__mass

    def get_price(self):
        return self.__price