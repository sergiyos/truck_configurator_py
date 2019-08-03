from truck import *
import time


def run_test(list_mass, list_wheel_formula, list_speed, truck):
    wheelbase = [3600, 3900]
    cabin_list = ['Над двигуном', 'За двигуном']
    body = ["Шасі", "Бортова платформа", "Сідельний тягач", "Самоскид", "Автоцистерна", "Фургон"]
    angle_list = [5, 10, 15, 20, 25, 30]
    iterations = 0
    for i in range(len(list_mass)):
        truck.set_mass(list_mass[i])
        for i in range(len(list_wheel_formula)):
            truck.set_wheel_configuration(list_wheel_formula[i])
            for i in range(len(wheelbase)):
                truck.set_wheel_base(wheelbase[i])
                for i in range(len(cabin_list)):
                    truck.set_cabin_type(cabin_list[i])
                    for i in range(len(body)):
                        truck.set_body_type(body[i])
                        for i in range(len(list_speed)):
                            truck.set_speed(list_speed[i])
                            for i in range(len(angle_list)):
                                truck.set_angle(angle_list[i])
                                truck.start()
                                print("---------------------------------")
                                print(truck.get_engine_item())
                                print(truck.get_chassis_item())
                                print(truck.get_cabin_item())
                                print(truck.get_body_item())
                                iterations += 1
                                print("---------------------------------")
    return iterations

start_time = time.time()
truck1 = Truck()
truck1.set_truck_type('Магістральний')
speed_list = [65, 75, 85, 95, 105, 115, 125, 135, 145]#
mass_list = [14000]
wheel_formula = ['4x2']
a = run_test(mass_list, wheel_formula, speed_list, truck1)

mass_list1 = [20000]
wheel_formula1 = ['6x2', '6x4']
b = run_test(mass_list1, wheel_formula1, speed_list, truck1)

speed_list2 = [65, 75, 85]# 40 t
mass_list2 = [40000]
wheel_formula2 = ['8x4']
c = run_test(mass_list2, wheel_formula2, speed_list2, truck1)

#Будівельні
truck2 = Truck()
truck2.set_truck_type('Будівельний')
wheel_formula3 = ['4x2', '4x4', '6x6']
d = run_test(mass_list, wheel_formula3, speed_list, truck2)

wheel_formula4 = ['6x2', '6x4', '6x6']
e = run_test(mass_list1, wheel_formula4, speed_list, truck2)

wheel_formula5 = ['6x6', '8x4', '8x8']
f = run_test(mass_list2, wheel_formula5, speed_list2, truck2)
mres = a+b+c
bres = d+e+f
print("Магістральні - %d" % mres)
print("Будівельні - %d" % bres)
result = a+b+c+d+e+f
print("Кількість ітерацій = %d" % result)
print("Час тестування %g секунди " % (time.time() - start_time))
