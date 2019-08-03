from database import *
from chassis import *
from cabin import *
from body import *
from engine import *


class Truck:

    __LIFTING_SPEED = 7  # Максимальна швидкість при підйомі
    __mass = None  # Повна масса
    __speed = None  # Максимальна швидкість
    __angle = None  # Кут підйому
    __Cx = None  # Аероденамічний коефіцієнт
    __H = None  # Висота
    __B = None  # Ширина
    __wheelConfiguration = None  # Колісна форма
    __Emp = None  # ККД трансмісії
    __truckType = None  # Тип автомобіля
    __bodyType = None  # Тип кузова
    __cabinType = None  # Тип кабіни
    __colorTruck = None  # Колір
    __wheelBase = None # Колісна база

    __kkdChassis = {"4x2": 0.9,
                    "4x4": 0.84,
                    "6x2": 0.9,
                    "6x4": 0.89,
                    "6x6": 0.78,
                    "8x4": 0.85,
                    "8x8": 0.74}  # ККД шасі

    __bodyCx = {# аероденамічні коефіцієнти кузовів
        "Шасі": 1,
        "Бортова платформа": 1.5,
        "Сідельний тягач": 1.4,
        "Самоскид": 1.45,
        "Автоцистерна": 1.2,
        "Фургон": 1.5
    }

    __model_name = None
    __name = {
        "Шасі": 3,
        "Бортова платформа": 3,
        "Сідельний тягач": 4,
        "Самоскид": 5,
        "Автоцистерна": 6,
        "Фургон": 7,
        14000: 4,
        20000: 5,
        40000: 6,
        "Магістральний" :1,
        "Будівельний": 2
    }

    __additional_items = None
    __truckPrice = None

    __engine_item = None
    __chassis_item = None
    __body_item = None
    __cabin_item = None

    def __init__(self):
        self.data = DataBase()# Запуск БД

    def set_truck_price(self):
        self.__truckPrice = self.NewEngine.get_price()+ self.NewBody.get_price()+ self.NewCabin.get_price()+ \
                            self.NewChassis.get_price()

    def set_model_name(self):
        self.__model_name = str(self.__name[self.__mass])+ str(self.__name[self.__bodyType]) + \
                            str(self.__name[self.__truckType]) + '1'

    def set_additional_items(self, additional_items):
        self.__additional_items = additional_items

    def set_wheel_base(self, wheelBase):
        self.__wheelBase = int(wheelBase)

    def set_color_truck(self, colorTruck):
        self.__colorTruck = colorTruck

    def set_cabin_type(self, cabinType):
        self.__cabinType = cabinType

    def set_body_type(self, bodyType):
        self.__bodyType = bodyType

    def set_wheel_configuration(self, wheelConfiguration):
        self.__wheelConfiguration = wheelConfiguration
        self.set_emp()

    def set_truck_type(self, truckType):
        self.__truckType = truckType

    def set_emp(self):
            self.__Emp = self.__kkdChassis[self.__wheelConfiguration]

    def set_mass(self, mass):
        self.__mass = int(mass)

    def set_speed(self, speed):
        self.__speed = int(speed)

    def set_angle(self, angle):
        self.__angle = int(angle)

    def set_cx(self, Cx):
        self.__Cx = float(Cx)

    def set_h(self, H):
        self.__H = int(H)

    def set_b(self, B):
        self.__B = int(B)

    def get_mass(self):
        return self.__mass

    def get_max_speed(self):
        return self.__speed

    def get_truck_type(self):
        return self.__truckType

    def get_wheel_configuration(self):
        return self.__wheelConfiguration

    def get_cabin_type(self):
        return self.__cabinType

    def get_body_type(self):
        return self.__bodyType

    def get_color(self):
        return self.__colorTruck

    def get_wheel_base(self):
        return self.__wheelBase

    def get_angle(self):
        return self.__angle

    def get_mass_truck(self):
        return self.NewEngine.get_mass()+self.NewChassis.get_mass()+self.NewCabin.get_mass()+self.NewBody.get_mass()

    def get_engine_item(self):
        return self.__engine_item

    def get_chassis_item(self):
        return self.__chassis_item

    def get_body_item(self):
        return self.__body_item

    def get_cabin_item(self):
        return self.__cabin_item

    def start(self):
        self.__chassis_selection()
        self.__cabin_selection()
        self.__body_selection()
        self.__Cx = self.NewCabin.get_Cx()*self.__bodyCx[self.NewBody.get_type_body()]# Встановлення Cx
        print("Cx = {0}".format(self.__Cx))

        #Висота
        if self.NewCabin.get_height() == self.NewBody.get_height():
            self.__H = self.NewCabin.get_height()
            print("Висота кабіни({0}) рівна "
                  "висоті кузова({1}),"
                  " тоді H = {2}".format(self.NewCabin.get_height(), self.NewBody.get_height(), self.__H))
        elif   self.NewCabin.get_height() > self.NewBody.get_height():
            self.__H = self.NewCabin.get_height()
            print("Висота кабіни({0}) більша "
                  "висоти кузова ({1}),"
                  " тоді H == {2}".format(self.NewCabin.get_height(), self.NewBody.get_height(), self.__H))
        else:
            self.__H = self.NewCabin.get_height()
            print("Висота кабіни({0}) менша "
                  "висоти кузова ({1}),"
                  " тоді H == {2}".format(self.NewCabin.get_height(), self.NewBody.get_height(), self.__H))
        # Ширина
        if self.NewCabin.get_width() == self.NewBody.get_width():
            self.__B = self.NewCabin.get_width()
            print("Ширина кабіни({0}) рівна ширині кузова({1}), тоді B = {2}".format(self.NewCabin.get_width(),
                                                self.NewBody.get_width(), self.__B))
        elif self.NewCabin.get_width() > self.NewBody.get_width():
            self.__B = self.NewCabin.get_width()
            print("Ширина кабіни({0}) більша ширини кузова({1}), тоді B = {2}".format(self.NewCabin.get_width(),
                                                self.NewBody.get_width(), self.__B))
        else:
            self.__B = self.NewBody.get_width()
            print("Ширина кабіни({0}) менша ширини кузова({1}), тоді B = {2}".format(self.NewCabin.get_width(),
                                                self.NewBody.get_width(), self.__B))

        self.__engine_calculation()
        self.set_model_name()
        self.set_truck_price()


    def __engine_calculation(self):

        m = self.__mass
        V = self.__speed / 3.6
        V2 = self.__LIFTING_SPEED / 3.6
        angle = self.__angle

        Fk1 = 0.01  # коефіцієнт опору кочення
        Fk2 = 7 * pow(10, -6)  # коефіцієнт опору кочення при великій швидкості руху
        Cx = self.__Cx  # аероденамічний коефіцієнт 0.5
        H = self.__H * pow(10, -3)  # висота 2500
        B = self.__B * pow(10, -3)  # ширина 2500
        A = H * B * 0.85  # лобова площа
        Nwxf = (m * 9.80665 * V * (Fk1 + Fk2 * pow(V, 2)) + Cx * A * 1.317 / 2 * pow(V, 3)) / self.__Emp
        Ni = (m * 9.80665 * (math.sin(angle * math.pi / 180) + math.cos(angle * math.pi / 180) * (
                Fk1 + Fk2 * pow(V2, 2))) * V2 + Cx * A * 1.317 / 2 * pow(V2, 3)) / self.__Emp
        print("----------------------------")
        print("Розрахунок потужності двигуна:")
        print("Масса = {0}".format(m))
        print("Кут підйому = {0}".format(angle))
        print("Швидкість = {0}".format(V))
        print("Cx = {0}".format(Cx))
        print("Висота = {0}".format(H))
        print("Ширина = {0}".format(B))
        print("Лобова площа = {0}".format(A))
        print("Nwxf = {0}".format(Nwxf))
        print("Ni = {0}".format(Ni))
        power = Ni
        if Nwxf > Ni: power = Nwxf
        print("Необхідна потужність = {0}".format(power))
        print("----------------------------")
        result = self.data.select_data("select * from двигуни where Максимальна_потужність >= {0}".format(power / 1000))

        result.sort(key=lambda i: i[3])
        result = result[0]
        self.NewEngine = Engine(result[1], result[2], result[3], result[4], result[5], result[6], result[7],
                              result[8], result[9], result[10])
        self.__engine_item = result
        print(result)

    def __chassis_selection(self):
        result = self.data.select_data("select * from шасі where Тип_перевезень = '{0}' and Колісна_формула = '{1}' "
                                       "and Колісна_база = '{2}'".format(self.__truckType, self.__wheelConfiguration, self.__wheelBase))
        result = result[0]
        self.NewChassis = Chassis(result[1], result[2], result[3], result[4], result[5], result[6], result[7],
                                 result[8],result[9], result[10])
        self.__chassis_item = result
        print(result)

    def __cabin_selection(self):
        result = self.data.select_data("select * from кабіни where Тип = '{0}' "
                                       "and Сфера_перевезень = '{1}'".format(self.__cabinType, self.__truckType))
        result = result[0]
        self.NewCabin = Cabin(result[1], result[2], result[3], result[4], result[5], result[6], result[7],
                              result[8])
        self.__cabin_item = result
        print(result)

    def __body_selection(self):
        if self.__bodyType == "Шасі":
            self.NewBody = Body("Chassis","Шасі", self.NewCabin.get_height(),self.NewCabin.get_width(),
                                0, 0)
        else:
            result = self.data.select_data("select * from кузови where Тип = '{0}'".format(self.__bodyType))
            result = result[0]
            self.NewBody = Body(result[1], result[2], result[3], result[4], result[5], result[6])
            print(result)
            self.__body_item = result


    def generate_result(self):

        self.list_result = []

        self.list_result.append("{0} {1}  Об'єкт {2} {3}".format(self.__truckType, self.NewBody.get_type_body().lower(),
                                                              self.__model_name, self.NewChassis.get_wheel_formula()))
        self.list_result.append("Separator")

        self.list_result.append("Повна маса, кг - %d" % self.__mass)
        self.list_result.append("Споряджена маса, кг - %d" % self.get_mass_truck())
        self.list_result.append("Максимальна швидкість, км/год - %d" % self.__speed)
        # Максимальна швидкість
        self.list_result.append("Separator")

        self.list_result.append("Двигун:")  # Назва
        self.list_result.append("   Марка - %s" % self.NewEngine.get_brand())  # Назва
        self.list_result.append("   Тип - дизельний 4-тактний %s" % self.NewEngine.get_configuration())  # конфігурація
        self.list_result.append("   Робочий об'єм, л - %g" % self.NewEngine.get_working_objective())  # Робочий об'єм
        self.list_result.append("   Максимальна ефективна потужність - %d к.с.(%d кВт), при %s об/хв" % (round(self.NewEngine.get_maximum_power()*1.3596),self.NewEngine.get_maximum_power(), self.NewEngine.get_rotate_power()))  # Потужність
        self.list_result.append("   Максимальний обертовий момент - %d Н·м (%d кГс·м), при %s об/хв" % (
        self.NewEngine.get_maximum_currency_moment(),self.NewEngine.get_maximum_currency_moment()/9.80665, self.NewEngine.get_rotate_currency_moment()))

        self.list_result.append("Separator")

        self.list_result.append("Шасі:")
        self.list_result.append("   Колісна база, мм - %s" % self.NewChassis.get_wheel_base())
        self.list_result.append("   Колісна формула - %s" % self.NewChassis.get_wheel_formula())  # Колісна формула
        self.list_result.append("   Тип підвіски - %s" % self.NewChassis.get_suspension().lower())
        self.list_result.append("   Габаритна довжина, мм - %s" % self.NewChassis.get_overall_length())
        self.list_result.append("   Шини - %s" % self.NewChassis.get_tires())


        self.list_result.append("Separator")

        self.list_result.append("Тип кабіни - %s" % self.NewCabin.get_typeCabin())
        self.list_result.append("Кузов - %s" % self.NewBody.get_type_body())
        self.list_result.append("Separator")
        self.list_result.append("Габаритні розміри, мм:")
        self.list_result.append("   Довжина - %d" % self.NewChassis.get_overall_length())
        self.list_result.append("   Ширина - %d" % self.__B)
        self.list_result.append("   Висота - %d" % self.__H)

        self.list_result.append("Separator")

        self.list_result.append("Маса агрегатів, кг:")
        self.list_result.append("    Двигун - %g" % self.NewEngine.get_mass())
        self.list_result.append("    Шасі - %g" % self.NewChassis.get_mass())
        self.list_result.append("    Кабіна - %g" % self.NewCabin.get_mass())
        if self.NewBody.get_type_body() != "Шасі":
            self.list_result.append("    Кузов - %g" % self.NewBody.get_mass())
        if self.__additional_items != None:
            if len(self.__additional_items) != 0:
                self.list_result.append("Separator")
                self.list_result.append("Додаткові елементи:")
                for i in range(len(self.__additional_items)):
                    self.list_result.append("   %s" % self.__additional_items[i])
        self.list_result.append("Separator")
        self.list_result.append("Колір - RAL2011")
        self.list_result.append("Separator")

        self.list_result1 = []
        self.list_result1.append("Підібрані комплектуючі:")
        self.list_result1.append("Двигун - %s" % str(self.__engine_item))
        self.list_result1.append("Шасі - %s" % str(self.__chassis_item))
        self.list_result1.append("Кабіна - %s" % str(self.__cabin_item))
        if self.NewBody.get_type_body() != "Шасі":
            self.list_result1.append("Кузов - %s" % str(self.__body_item))
        self.list_result1.append("Separator")
        self.list_result1.append("Орієнтована ціна комплектуючих - %d" % self.__truckPrice)



