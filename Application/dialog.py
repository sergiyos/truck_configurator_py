from tkinter import *
from functools import partial
from tkinter import ttk
from tkinter import messagebox
from truck import *


class Dialog:

    fontA = 'Verdana 12'
    unselected = "SystemButtonFace"
    selected = "#80ff80"
    __currentFrame = 0

    def __init__(self, master):

        self.newTruck = Truck()

        self.top = Toplevel(master)
        self.top.title("Конфігурація")
        self.top.width = 700
        height = 620
        self.top.x_coordinate = (master.winfo_screenwidth()/2)-(self.top.width/2)
        self.top.y_coordinate = (master.winfo_screenheight()/2)-(height/2)
        self.top.geometry("%dx%d+%d+%d" % (self.top.width, height,
                                           self.top.x_coordinate, self.top.y_coordinate))
        self.top.resizable(False, False)
        self.top.iconbitmap("img\\icons\\icon.ico")
        self.top.focus()
        # Основні блоки
        self.mainFrame = Frame(self.top, height=520, width=self.top.width)
        self.buttonFrame = Frame(self.top, height=100, width=self.top.width)
        self.mainFrame.grid(row=0, column=0)
        self.buttonFrame.grid(row=1, column=0)
        # Основні переходи
        self.buttonBack = Button(self.buttonFrame, text="Назад", state=DISABLED, width=30, height=2,
                                     bg="#c2d6d6",font=self.fontA, command=self.button_back)
        self.buttonNext = Button(self.buttonFrame, text="Далі", width=30, height=2,
                                     bg="#c2d6d6",font=self.fontA, command=self.button_next)
        self.buttonBack.grid(row=0, column=0, padx=15, pady=20)
        self.buttonNext.grid(row=0, column=1, padx=15, pady=20)
        # 1 Фрейм
        self.__currentFrame = 0
        # 1 Фрейм
        self.frame1 = Frame(self.top, height=520, width=self.top.width)
        self.frame1Label = Label(self.frame1, text="Сфера перевезень:", font=self.fontA)
        self.frame1Label.grid(row=0, column=0, padx=5, pady=15, columnspan=2)
        self.frame1Button = []
        self.frame1Image = []
        self.frame1ButtonText = ["Магістральні", "Будівельні"]
        self.frame1ImagePath = [PhotoImage(file="img\\truck\\M.png"), PhotoImage(file="img\\truck\\B.png")]
        for i in range(len(self.frame1ButtonText)):
            self.frame1Image.append(Label(self.frame1, image=self.frame1ImagePath[i]))
            self.frame1Button.append(Button(self.frame1, width=25, height=2, text=self.frame1ButtonText[i],
                                            font=self.fontA, command=partial(self.frame1_button, i)))
            self.frame1Image[i].grid(row=1, column=i, padx=5, pady=25)
            self.frame1Button[i].grid(row=2, column=i, padx=5, pady=0)
        self.frame1.grid(row=0, column=0)
        #2 Фрейм
        self.frame2 = Frame(self.top, height=520, width=self.top.width)
        self.frame2Label = Label(self.frame2, text="Клас вантажного автомобіля:", font=self.fontA)
        self.frame2Label.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame2Button = []
        self.frame2ButtonText = ["8 - 14 T", "15 - 20 T", "21 - 40 T"]
        for i in range(len(self.frame2ButtonText)):
            self.frame2Button.append(Button(self.frame2, width=25, height=2, text=self.frame2ButtonText[i],
                                            font=self.fontA, command=partial(self.frame2_button, i)))

            self.frame2Button[i].grid(row=i+1, column=0, padx=5, pady=5)

        self.frame3Type = None
        # 3A фрейм
        self.frame3text = "Колісна формула:"
        self.frame3A = Frame(self.top, height=520, width=self.top.width)
        self.frame3ALabel = Label(self.frame3A, text=self.frame3text, font=self.fontA)
        self.frame3ALabel.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame3AButton = []
        self.frame3AImage = []
        self.frame3AButtonText = ["4x2"]
        self.frame3AImagePath = [PhotoImage(file="img\\wheel\\4x2.png")]
        for i in range(len(self.frame3AButtonText)):
            self.frame3AImage.append(Label(self.frame3A, image=self.frame3AImagePath[i]))
            self.frame3AButton.append(Button(self.frame3A, width=25, height=2, text=self.frame3AButtonText[i],
                                             font=self.fontA, command=partial(self.frame3a_button, i)))
            self.frame3AImage[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame3AButton[i].grid(row=i + 1, column=1, padx=5, pady=5)

        # 3B фрейм
        self.frame3B = Frame(self.top, height=520, width=self.top.width)
        self.frame3BLabel = Label(self.frame3B, text=self.frame3text, font=self.fontA)
        self.frame3BLabel.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame3BButton = []
        self.frame3BImage = []
        self.frame3BButtonText = ["6x2", "6x4"]
        self.frame3BImagePath = [ PhotoImage(file="img\\wheel\\6x2.png"), PhotoImage(file="img\\wheel\\6x4.png")]
        for i in range(len(self.frame3BButtonText)):
            self.frame3BImage.append(Label(self.frame3B, image=self.frame3BImagePath[i]))
            self.frame3BButton.append(Button(self.frame3B, width=25, height=2, text=self.frame3BButtonText[i],
                                            font=self.fontA, command=partial(self.frame3b_button, i)))
            self.frame3BImage[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame3BButton[i].grid(row=i + 1, column=1, padx=5, pady=5)

        # 3C фрейм
        self.frame3C = Frame(self.top, height=520, width=self.top.width)
        self.frame3CLabel = Label(self.frame3C, text=self.frame3text, font=self.fontA)
        self.frame3CLabel.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame3CButton = []
        self.frame3CImage = []
        self.frame3CButtonText = ["8x4"]
        self.frame3CImagePath = [PhotoImage(file="img\\wheel\\8x4.png")]
        for i in range(len(self.frame3CButtonText)):
            self.frame3CImage.append(Label(self.frame3C, image=self.frame3CImagePath[i]))
            self.frame3CButton.append(Button(self.frame3C, width=25, height=2, text=self.frame3CButtonText[i],
                                             font=self.fontA, command=partial(self.frame3c_button, i)))
            self.frame3CImage[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame3CButton[i].grid(row=i + 1, column=1, padx=5, pady=5)

        # 3D фрейм
        self.frame3D = Frame(self.top, height=520, width=self.top.width)
        self.frame3DLabel = Label(self.frame3D, text=self.frame3text, font=self.fontA)
        self.frame3DLabel.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame3DButton = []
        self.frame3DImage = []
        self.frame3DButtonText = ["4x2", "4x4", "6x6"]
        self.frame3DImagePath = [PhotoImage(file="img\\wheel\\4x2.png"), PhotoImage(file="img\\wheel\\4x4.png"),
                                 PhotoImage(file="img\\wheel\\6x6.png")]
        for i in range(len(self.frame3DButtonText)):
            self.frame3DImage.append(Label(self.frame3D, image=self.frame3DImagePath[i]))
            self.frame3DButton.append(Button(self.frame3D, width=25, height=2, text=self.frame3DButtonText[i],
                                             font=self.fontA, command=partial(self.frame3d_button, i)))
            self.frame3DImage[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame3DButton[i].grid(row=i + 1, column=1, padx=5, pady=5)

        # 3E фрейм
        self.frame3E = Frame(self.top, height=520, width=self.top.width)
        self.frame3ELabel = Label(self.frame3E, text=self.frame3text, font=self.fontA)
        self.frame3ELabel.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame3EButton = []
        self.frame3EImage = []
        self.frame3EButtonText = ["6x2", "6x4", "6x6"]
        self.frame3EImagePath = [PhotoImage(file="img\\wheel\\6x2.png"), PhotoImage(file="img\\wheel\\6x4.png"),
                                 PhotoImage(file="img\\wheel\\6x6.png")]
        for i in range(len(self.frame3EButtonText)):
            self.frame3EImage.append(Label(self.frame3E, image=self.frame3EImagePath[i]))
            self.frame3EButton.append(Button(self.frame3E, width=25, height=2, text=self.frame3EButtonText[i],
                                             font=self.fontA, command=partial(self.frame3e_button, i)))
            self.frame3EImage[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame3EButton[i].grid(row=i + 1, column=1, padx=5, pady=5)

        # 3F фрейм
        self.frame3F = Frame(self.top, height=520, width=self.top.width)
        self.frame3FLabel = Label(self.frame3F, text=self.frame3text, font=self.fontA)
        self.frame3FLabel.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame3FButton = []
        self.frame3FImage = []
        self.frame3FButtonText = ["6x6", "8x4", "8x8"]
        self.frame3FImagePath = [PhotoImage(file="img\\wheel\\6x6.png"), PhotoImage(file="img\\wheel\\8x4.png"),
                                 PhotoImage(file="img\\wheel\\8x8.png")]
        for i in range(len(self.frame3FButtonText)):
            self.frame3FImage.append(Label(self.frame3F, image=self.frame3FImagePath[i]))
            self.frame3FButton.append(Button(self.frame3F, width=25, height=2, text=self.frame3FButtonText[i],
                                             font=self.fontA, command=partial(self.frame3f_button, i)))
            self.frame3FImage[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame3FButton[i].grid(row=i + 1, column=1, padx=5, pady=5)

        # 4 фрейм
        self.frame4 = Frame(self.top, height=520, width=self.top.width)
        self.frame4Label = Label(self.frame4, text="Колісна база:", font=self.fontA)
        self.frame4Label.grid(row=0, column=0, padx=5, pady=30, columnspan=4)
        self.frame4Image1Path = PhotoImage(file="img\\base\\wheel_base.png")
        self.frame4Image2Path = PhotoImage(file="img\\base\\wheel_base2.png")
        self.frame4Image = Label(self.frame4, image=self.frame4Image1Path)
        self.frame4Image.grid(row=1, column=0, padx=5, pady=30, columnspan=2)
        self.frame4Button = []
        self.frame4ButtonText = ["3600", "3900"]
        for i in range(len(self.frame4ButtonText)):
            self.frame4Button.append(Button(self.frame4, width=25, height=2, text=self.frame4ButtonText[i],
                                            font=self.fontA, command=partial(self.frame4_button, i)))
            self.frame4Button[i].grid(row=2, column=i, padx=5, pady=5)

        # Фрейм 5
        self.frame5 = Frame(self.top, height=520, width=self.top.width)
        self.frame5Label = Label(self.frame5, text="Тип кабіни:", font=self.fontA)
        self.frame5Label.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame5Button = []
        self.frame5Image = []
        self.frame5ButtonText = ["За двигуном", "Над двигуном"]
        self.frame5ImagePath = [PhotoImage(file="img\\cabin\\Type_1.png"), PhotoImage(file="img\\cabin\\Type_2.png")]
        for i in range(len(self.frame5ButtonText)):
            self.frame5Image.append(Label(self.frame5, image=self.frame5ImagePath[i]))
            self.frame5Button.append(Button(self.frame5, width=25, height=2, text=self.frame5ButtonText[i],
                                            font=self.fontA, command=partial(self.frame5_button, i)))
            self.frame5Image[i].grid(row=1, column=i, padx=5, pady=0)
            self.frame5Button[i].grid(row=2, column=i, padx=5, pady=5)

        # Фрейм 6
        self.frame6 = Frame(self.top, height=520, width=self.top.width)
        self.frame6Label = Label(self.frame6, text="Тип кузова:", font=self.fontA)
        self.frame6Label.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame6Button = []
        self.frame6Image = []
        self.frame6ButtonText = ["Шасі", "Бортова платформа", "Сідельний тягач", "Самоскид", "Автоцистерна", "Фургон"]
        self.frame6ImagePath = [PhotoImage(file="img\\body\\Chassis.png"), PhotoImage(file="img\\body\\Platform.png"),
                                PhotoImage(file="img\\body\\Truck.png"), PhotoImage(file="img\\body\\Tipper.png"),
                                PhotoImage(file="img\\body\\Tank.png"),
                                PhotoImage(file="img\\body\\Trunk.png")]
        for i in range(len(self.frame6ButtonText)):
            self.frame6Image.append(Label(self.frame6, image=self.frame6ImagePath[i]))
            self.frame6Button.append(Button(self.frame6, width=25, height=2, text=self.frame6ButtonText[i],
                                            font=self.fontA, command=partial(self.frame6_button, i)))
            self.frame6Image[i].grid(row=i + 1, column=0, padx=5, pady=0)
            self.frame6Button[i].grid(row=i + 1, column=1, padx=5, pady=5)


        # Фрейм 7
        self.frame7 = Frame(self.top, height=520, width=self.top.width)
        self.frame7Label = Label(self.frame7, text="Додаткові елементи:", font=self.fontA)
        self.frame7Label.grid(row=0, column=0, padx=5, pady=30, columnspan=2)
        self.frame7Check = []
        self.frame7Image = []
        self.frame7Var = []

        s = ttk.Style()
        s.configure('my.TCheckbutton', font=('Verdana', 12))

        self.frame7CheckText = ["1. Верхній обтічник (драгфойлер)", "2. Вертикальні дефлектори", "3. Бампер-спойлер",
                                "4. Боковий обтічник", "5. Бокові дефлектори", "6. Збільшена висота кабіни",
                                "7. Збільшена довжина кабіни", "8. Козирок"]
        self.frame7ImagePath = PhotoImage(file="img\\additional_elements.png")
        self.frame7Image = Label(self.frame7, image=self.frame7ImagePath)
        self.frame7Image.grid(row=1, column=0, padx=5, pady=0, rowspan=8)
        for i in range(len(self.frame7CheckText)):
            self.frame7Var.append(StringVar())
            self.frame7Check.append(ttk.Checkbutton(self.frame7, text=self.frame7CheckText[i], var=self.frame7Var[i],
                        style='my.TCheckbutton',onvalue=self.frame7CheckText[i], offvalue=''))
            self.frame7Check[i].grid(row=i + 1, column=1, padx=5, pady=5, sticky="w")

        # Фрейм 8
        self.frame8 = Frame(self.top, height=520, width=self.top.width)
        self.frame8Label = Label(self.frame8, text="Максимальна швидкість км/год ", font=self.fontA)
        self.frame8Label.grid(row=0, column=0, padx=25, pady=50)
        self.frame8Values = 65, 75, 85, 95, 105, 115, 125, 135, 145
        self.frame8Values2 = 65, 75, 85
        self.frame8List = ttk.Combobox(self.frame8, values=self.frame8Values, state='readonly', font=self.fontA)
        self.frame8List.set(65)
        self.frame8List.grid(row=1, column=0, padx=5, pady=0)

        # Фрейм 9
        self.frame9 = Frame(self.top, height=520, width=self.top.width)
        self.frame9Label = Label(self.frame9, text="Максимальний кут підйому, град.", font=self.fontA)
        self.frame9Label.grid(row=0, column=0, padx=25, pady=50)
        self.frame9Values = 5, 10, 15, 20, 25, 30
        self.frame9List = ttk.Combobox(self.frame9, values=self.frame9Values, state='readonly', font=self.fontA)
        self.frame9List.set(5)
        self.frame9List.grid(row=1, column=0, padx=5, pady=0)

        # Фрейм 10
        self.frame10 = Frame(self.top, height=520, width=self.top.width)
        self.frame10Label = Label(self.frame10, text="Оберіть колір кабіни", font=self.fontA)
        self.frame10Label.grid(row=0, column=0, padx=5, pady=5, columnspan=15)
        self.frame10Image = PhotoImage(file="img\\Truck.png")
        self.frame10LabelImage = Label(self.frame10, image=self.frame10Image)
        self.frame10LabelImage.grid(row=1, column=0, padx=5, pady=50, columnspan=15)
        self.frame10Button = []
        self.frame10ColorList = ["#e1a100", "#e86f00", "#840914", "#500002", "#af0001", "#003c78", "#0088b5",
                                 "#00588a", "#316650", "#003a26", "#5b972d", "#eee4d3", "#040405", "#9fa3a3",
                                 "#748591"]
        for i in range(len(self.frame10ColorList)):
            self.frame10Button.append(Button(self.frame10, width=5, height=3, bg=self.frame10ColorList[i],
                                             command=partial(self.frame10_button, i)))
            self.frame10Button[i].grid(row=2, column=i)

        self.frameList = [self.frame1, self.frame2, self.frame3A, self.frame4, self.frame5, self.frame6,
                          self.frame7, self.frame8, self.frame9, self.frame10]

        self.choiceList = [False, False, False, False, False, False, False, False, False, False]

    def button_next(self):

        if self.__currentFrame == 6:
            self.choiceList[self.__currentFrame] = True
            items = []
            for i in range(len(self.frame7Var)):
                if self.frame7Var[i].get() != '':
                    items.append(self.frame7Var[i].get()[3:])
                    #print(self.frame7Var[i].get())
            if len(items) != 0:
                self.newTruck.set_additional_items(items)

        if self.__currentFrame == 7:
            self.choiceList[self.__currentFrame] = True
            self.newTruck.set_speed(self.frame8List.get())
            print(self.newTruck.get_max_speed())# Швидкість

        if self.__currentFrame == 8:
            self.choiceList[self.__currentFrame] = True
            self.newTruck.set_angle(self.frame9List.get())
            print(self.newTruck.get_angle())# Кут підйому

        if self.choiceList[self.__currentFrame] is False:
            messagebox.showwarning("Увага", "Оберіть варіант конфігурації!", parent=self.top)
        else:

            if self.__currentFrame != len(self.frameList) - 1:
                self.frameList[self.__currentFrame].grid_remove()
                self.frameList[self.__currentFrame + 1].grid(row=0, column=0)
                self.__currentFrame += 1
                self.buttonBack.config(state="normal")
                if self.__currentFrame == len(self.frameList) - 1:
                    self.buttonNext.config(text="Готово")
            else:
                print("Закінчення вибору конфігурації")
                print("----------------------------")
                self.newTruck.start()
                self.accept()

        # Кнопка назад

    def button_back(self):

        if self.__currentFrame == len(self.frameList) - 1:
            self.buttonNext.config(text="Далі")
        self.frameList[self.__currentFrame].grid_remove()
        self.choiceList[self.__currentFrame] = False
        self.frameList[self.__currentFrame - 1].grid(row=0, column=0)
        self.__currentFrame -= 1
        if self.__currentFrame == 0:
            self.buttonBack.config(state=DISABLED)

    def frame1_button(self, n):
        for i in range(len(self.frame1Button)):
            if i == n:
                self.frame1Button[i].config(bg=self.selected)
                self.frame3Type = n
                self.choiceList[0] = True

                if n == 0:
                    self.newTruck.set_truck_type("Магістральний")
                    print(self.newTruck.get_truck_type())
                else:
                    self.newTruck.set_truck_type("Будівельний")
                    print(self.newTruck.get_truck_type())

            else:
                self.frame1Button[i].config(bg=self.unselected)

    def frame2_button(self, n):
        for i in range(len(self.frame2Button)):
            if i == n:
                self.frame2Button[i].config(bg=self.selected)
                self.frame3_type(n)
                self.choiceList[1] = True

                if n == 0:
                    self.newTruck.set_mass(14000)
                    print(self.newTruck.get_mass())
                    self.frame8List.config(values=self.frame8Values)
                elif n == 1:
                    self.newTruck.set_mass(20000)
                    print(self.newTruck.get_mass())
                    self.frame8List.config(values=self.frame8Values)

                else:
                    self.newTruck.set_mass(40000)
                    print(self.newTruck.get_mass())
                    self.frame8List.config(values=self.frame8Values2)
                    self.frame8List.set(65)


            else:
                self.frame2Button[i].config(bg=self.unselected)

    def frame3_type(self, num):
        if self.frame3Type == 0:
            if num == 0:
                self.frameList[2] = self.frame3A
            if num == 1:
                self.frameList[2] = self.frame3B
            if num == 2:
                self.frameList[2] = self.frame3C
        else:
            if num == 0:
                self.frameList[2] = self.frame3D
            if num == 1:
                self.frameList[2] = self.frame3E
            if num == 2:
                self.frameList[2] = self.frame3F

    def frame3a_button(self, n):
        for i in range(len(self.frame3AButton)):
            if i == n:
                self.frame3AButton[i].config(bg=self.selected)
                self.choiceList[2] = True
                if n == 0:
                    self.newTruck.set_wheel_configuration("4x2")
                    print(self.newTruck.get_wheel_configuration())

            else:
                self.frame3AButton[i].config(bg=self.unselected)

    def frame3b_button(self, n):
        for i in range(len(self.frame3BButton)):
            if i == n:
                self.frame3BButton[i].config(bg=self.selected)
                self.choiceList[2] = True
                if n == 0:
                    self.newTruck.set_wheel_configuration("6x2")
                    print(self.newTruck.get_wheel_configuration())
                else:
                    self.newTruck.set_wheel_configuration("6x4")
                    print(self.newTruck.get_wheel_configuration())

            else:
                self.frame3BButton[i].config(bg=self.unselected)

    def frame3c_button(self, n):
        for i in range(len(self.frame3CButton)):
            if i == n:
                self.frame3CButton[i].config(bg=self.selected)
                self.choiceList[2] = True
                if n == 0:
                    self.newTruck.set_wheel_configuration("8x4")
                    print(self.newTruck.get_wheel_configuration())
            else:
                self.frame3CButton[i].config(bg=self.unselected)

    def frame3d_button(self, n):
        for i in range(len(self.frame3DButton)):
            if i == n:
                self.frame3DButton[i].config(bg=self.selected)
                self.choiceList[2] = True

                if n == 0:
                    self.newTruck.set_wheel_configuration("4x2")
                    print(self.newTruck.get_wheel_configuration())
                elif n == 1:
                    self.newTruck.set_wheel_configuration("4x4")
                    print(self.newTruck.get_wheel_configuration())
                else:
                    self.newTruck.set_wheel_configuration("6x6")
                    print(self.newTruck.get_wheel_configuration())

            else:
                self.frame3DButton[i].config(bg=self.unselected)

    def frame3e_button(self, n):
        for i in range(len(self.frame3EButton)):
            if i == n:
                self.frame3EButton[i].config(bg=self.selected)
                self.choiceList[2] = True

                if n == 0:
                    self.newTruck.set_wheel_configuration("6x2")
                    print(self.newTruck.get_wheel_configuration())
                elif n == 1:
                    self.newTruck.set_wheel_configuration("6x4")
                    print(self.newTruck.get_wheel_configuration())
                else:
                    self.newTruck.set_wheel_configuration("6x6")
                    print(self.newTruck.get_wheel_configuration())

            else:
                self.frame3EButton[i].config(bg=self.unselected)

    def frame3f_button(self, n):
        for i in range(len(self.frame3FButton)):
            if i == n:
                self.frame3FButton[i].config(bg=self.selected)
                self.choiceList[2] = True

                if n == 0:
                    self.newTruck.set_wheel_configuration("6x6")
                    print(self.newTruck.get_wheel_configuration())
                elif n == 1:
                    self.newTruck.set_wheel_configuration("8x4")
                    print(self.newTruck.get_wheel_configuration())
                else:
                    self.newTruck.set_wheel_configuration("8x8")
                    print(self.newTruck.get_wheel_configuration())
            else:
                self.frame3FButton[i].config(bg=self.unselected)

    def frame4_button(self, n):
        for i in range(len(self.frame4Button)):
            if i == n:
                self.frame4Button[i].config(bg=self.selected)
                self.choiceList[3] = True
                if n == 0:
                    self.newTruck.set_wheel_base(3600)
                    print(self.newTruck.get_wheel_base())
                    self.frame4Image.config(image=self.frame4Image1Path)
                else:
                    self.newTruck.set_wheel_base(3900)
                    print(self.newTruck.get_wheel_base())
                    self.frame4Image.config(image=self.frame4Image2Path)
            else:
                self.frame4Button[i].config(bg=self.unselected)

    def frame5_button(self, n):
        for i in range(len(self.frame5Button)):
            if i == n:
                self.frame5Button[i].config(bg=self.selected)
                self.choiceList[4] = True
                if n == 0:
                    self.newTruck.set_cabin_type("За двигуном")
                    print(self.newTruck.get_cabin_type())
                else:
                    self.newTruck.set_cabin_type("Над двигуном")
                    print(self.newTruck.get_cabin_type())
            else:
                self.frame5Button[i].config(bg=self.unselected)

    def frame6_button(self, n):
        for i in range(len(self.frame6Button)):
            if i == n:
                self.frame6Button[i].config(bg=self.selected)
                self.choiceList[5] = True
                if n == 0:
                    self.newTruck.set_body_type("Шасі")
                    print(self.newTruck.get_body_type())
                elif n == 1:
                    self.newTruck.set_body_type("Бортова платформа")
                    print(self.newTruck.get_body_type())
                elif n == 2:
                    self.newTruck.set_body_type("Сідельний тягач")
                    print(self.newTruck.get_body_type())
                elif n == 3:
                    self.newTruck.set_body_type("Самоскид")
                    print(self.newTruck.get_body_type())
                elif n == 4:
                    self.newTruck.set_body_type("Автоцистерна")
                    print(self.newTruck.get_body_type())
                else:
                    self.newTruck.set_body_type("Фургон")
                    print(self.newTruck.get_body_type())

            else:
                self.frame6Button[i].config(bg=self.unselected)

    def frame10_button(self, n):
        for i in range(len(self.frame10Button)):
            if i == n:
                self.frame10Button[i].config(relief="solid")
                self.choiceList[9] = True
                self.newTruck.set_color_truck(self.frame10ColorList[i])
                print(self.newTruck.get_color())
            else:
                self.frame10Button[i].config(relief="raised")

    def go(self): # Передача потоку запуск діалогу
        self.newValue = None
        self.top.grab_set()
        self.top.focus_set()
        self.top.wait_window()
        return self.newValue

    def accept(self):    # Відправляємо результат
        self.newValue = self.newTruck
        self.top.destroy()


