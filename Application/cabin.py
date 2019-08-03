
class Cabin:

    def __init__(self, name, typeCabin, Cx, height, width, transportationType, mass, price):

        self.__name = name # назва
        self.__typeCabin = typeCabin # тип
        self.__Cx = Cx # аеродинамічний коефіцієнт
        self.__height = height # висота
        self.__width = width # ширина
        self.__transportationType = transportationType # тип перевезень
        self.__mass = mass # маса
        self.__price = price # ціна

    def get_name(self):
        return self.__name

    def get_typeCabin(self):
        return self.__typeCabin

    def get_Cx(self):
        return self.__Cx

    def get_height(self):
        return self.__height

    def get_width(self):
        return self.__width

    def get_transportationType(self):
        return self.__transportationType

    def get_mass(self):
        return self.__mass

    def get_price(self):
        return self.__price