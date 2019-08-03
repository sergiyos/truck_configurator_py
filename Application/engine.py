import math
import matplotlib.pyplot as plt


class Engine:

    def __init__(self, brand, configuration, maximum_power, rotate_power, maximum_currency_moment,
                 rotate_currency_moment, working_objective, overall_dimensions, mass, price):

        self.__brand = brand # марка
        self.__configuration = configuration #конфігурація
        self.__maximum_power = maximum_power # максимальна_потужність
        self.__rotate_power = rotate_power # оберти_потужності
        self.__maximum_currency_moment = maximum_currency_moment # максимальний_крутний_момент
        self.__rotate_currency_moment = rotate_currency_moment # оберти_крутного_моменту
        self.__working_objective = working_objective # робочий_обєм
        self.__overall_dimensions = overall_dimensions #габаритні_розміри
        self.__mass = mass # маса
        self.__price = price # ціна

    def get_brand(self):
        return self.__brand

    def get_configuration(self):
        return self.__configuration

    def get_maximum_power(self):
        return self.__maximum_power

    def get_rotate_power(self):
        return self.__rotate_power

    def get_maximum_currency_moment(self):
        return self.__maximum_currency_moment

    def get_rotate_currency_moment(self):
        return self.__rotate_currency_moment

    def get_working_objective(self):
        return self.__working_objective

    def get_overall_dimensions(self):
        return self.__overall_dimensions

    def get_mass(self):
        return self.__mass

    def get_price(self):
        return self.__price

    #Швидкісна характеристика
    def power_band(self):

        n_N = float(self.__rotate_power)# оберти_потужності

        moment = self.__rotate_currency_moment
        if '-' in moment:
            temp = moment.split("-")
            moment = (int(temp[0]) + int(temp[1])) / 2

        n_T = float(moment)# оберти_крутного_моменту

        T_max = self.__maximum_currency_moment # максимальний_крутний_момент
        N_max = self.__maximum_power * 1000 # максимальна_потужність

        W_n_N = (math.pi * n_N) / 30
        W_n_T = (math.pi * n_T) / 30

        T_N = N_max / W_n_N

        K_w = W_n_N / W_n_T
        K_t = T_max / T_N

        a = (K_w * K_t * (2 - K_w) - 1) / (K_w * (2 - K_w) - 1)
        b = (-2 * K_w * (K_t - 1)) / (K_w * (2 - K_w) - 1)
        c = (pow(K_w, 2) * (K_t - 1)) / (K_w * (2 - K_w) - 1)

        print(a + b + c)

        N1 = N_max / W_n_N
        N2 = N_max / pow(W_n_N, 2)
        N3 = N_max / pow(W_n_N, 3)

        print("N1 = {0}".format(N1))
        print("N2 = {0}".format(N2))
        print("N3 = {0}".format(N3))

        print(W_n_N)

        W_min = W_n_N / 3
        print(W_min)

        self.x = []
        self.y = []
        self.z = []

        while W_min < W_n_N:
            Ne = a * N1 * W_min + b * N2 * pow(W_min, 2) + c * N3 * pow(W_min, 3)
            Te = a * N1 + b * N2 * W_min + c * N3 * pow(W_min, 2)
            self.x.append(W_min)
            self.y.append(Ne * 10 ** -3)
            self.z.append(Te)
            W_min += 1
        for i in range(len(self.x)):
            self.x[i] = self.x[i] * 30 / math.pi
           #Графік
        plt.plot(self.x, self.y, color="blue")
        plt.xlabel("Частота обертання колінчастого вала, об/хв")
        plt.ylabel("Ефективна потужність, кВт", color="blue")
        plt.tick_params(axis='y', labelcolor="blue")
        plt.grid()
        plt.twinx()
        plt.plot(self.x, self.z, color="red")
        plt.ylabel("Ефективний обертовий момент, Н·м", color="red")
        plt.tick_params(axis='y', labelcolor="red")
        plot_file = "res\\power_band\\plot.png"
        plt.savefig(plot_file, transparent=True, dpi=70)
        plt.cla() # Очистити axis
        plt.clf() # Очистити figure







