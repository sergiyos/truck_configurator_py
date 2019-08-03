
class Chassis:

    def __init__(self, name, wheel_formula, wheel_base, overall_length, rut, tires, transportationType,
                 suspension, mass, price):
        self.__name = name # назва
        self.__wheel_formula = wheel_formula # косісна формула
        self.__wheel_base = wheel_base # колісна база
        self.__overall_length = overall_length # габаритна довжина
        self.__rut = rut # колія
        self.__tires = tires # шини
        self.__transportationType = transportationType # тип перевезень
        self.__suspension = suspension # підвіска
        self.__mass = mass # маса
        self.__price = price # ціна

    def get_name(self):
        return self.__name

    def get_wheel_formula(self):
        return self.__wheel_formula

    def get_wheel_base(self):
        return self.__wheel_base

    def get_overall_length(self):
        return self.__overall_length

    def get_rut(self):
        return self.__rut

    def get_tires(self):
        return self.__tires

    def get_transportationType(self):
        return self.__transportationType

    def get_suspension(self):
        return self.__suspension

    def get_mass(self):
        return self.__mass

    def get_price(self):
        return self.__price

