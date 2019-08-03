import pickle
from tkinter.filedialog import askopenfilename
from dialog import *
from create_pdf import *


class ScrolledFrame(Frame):

    def __init__(self, parent, *args, **kw):
        Frame.__init__(self, parent, *args, **kw)
        scrollbar = Scrollbar(self, orient=VERTICAL)
        scrollbar.pack(fill=Y, side=RIGHT, expand=FALSE)
        canvas = Canvas(self, bd=0, highlightthickness=0,
                        yscrollcommand=scrollbar.set)
        canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)
        scrollbar.config(command=canvas.yview)
        canvas.xview_moveto(0)
        canvas.yview_moveto(0)
        self.interior = interior = Frame(canvas, bg="#f0f5f5")
        interior_id = canvas.create_window(0, 0, window=interior,
                                           anchor=NW)

        def _configure_interior(event):
            size = (interior.winfo_reqwidth(), interior.winfo_reqheight())
            canvas.config(scrollregion="0 0 %s %s" % size)
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.config(width=interior.winfo_reqwidth())
        interior.bind('<Configure>', _configure_interior)

        def _configure_canvas(event):
            if interior.winfo_reqwidth() != canvas.winfo_width():
                canvas.itemconfigure(interior_id, width=canvas.winfo_width())
        canvas.bind('<Configure>', _configure_canvas)


class Main:

    fontM = 'Verdana 12'

    def __init__(self, master):

        self.master = master
        master.title("Головне меню")
        self.width = 1280
        height = 540
        x_coordinate = (self.master.winfo_screenwidth() / 2) - (self.width / 2)
        y_coordinate = (self.master.winfo_screenheight() / 2) - (height / 2)
        self.master.geometry("%dx%d+%d+%d" % (self.width, height, x_coordinate, y_coordinate))
        master.resizable(False, False)
        master.iconbitmap("img\\icons\\icon.ico")
        master.protocol('WM_DELETE_WINDOW', self.window_deleted)

        self.mainMenu = Menu(master)
        master.configure(menu=self.mainMenu)
        self.firstItem = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Файл", menu=self.firstItem)
        self.firstItem.add_command(label="Створити", command=self.start_dialog)  # enter dialog
        self.firstItem.add_command(label="Відкрити", command=self.open_file)
        self.firstItem.add_command(label="Зберегти", command=self.save_file)
        self.firstItem.add_separator()
        self.firstItem.add_command(label="Закрити", command=self.close_result)
        self.firstItem.add_separator()
        self.firstItem.add_command(label="Вихід", command=self.window_deleted)

        self.view = Menu(self.mainMenu, tearoff=0)
        self.mainMenu.add_cascade(label="Документація", menu=self.view)
        self.view.add_command(label="Сформувати документ", command=self.create_pdf)


        self.mainFrame = ScrolledFrame(master)
        self.mainFrame.pack(fill=BOTH, expand=1)

        # Статус Бар
        self.statusBar = Label(self.master, text="", bd=1, relief=SUNKEN, anchor=W)
        self.statusBar.pack(side=BOTTOM, fill=X)

    def start_dialog(self):
        self.dialog = Dialog(self.master)
        self.truck = self.dialog.go()
        if self.truck:
            print("Main - {0}".format(self.truck))
            self.load_result()

    def window_deleted(self):
        result = messagebox.askquestion("Вихід", "Ви впевнені що бажаєте вийти?")
        if result == 'yes':
            self.master.quit()
            #sys.exit()
        else:
            pass

    def close_result(self):
        if hasattr(self, 'information'):
            self.information.destroy()
            self.statusBar.config(text="")

    def load_result(self):
        self.close_result()
        self.information = Frame(self.mainFrame.interior, width=self.width, bg="#f0f5f5")
        self.information.grid(row=0, column=0, padx=25, pady=5, sticky="w")
        self.label = []
        self.truck.generate_result()

        for i in range(len(self.truck.list_result)):
            if self.truck.list_result[i] != "Separator":
                self.label.append(Label(self.information, text=self.truck.list_result[i],bg="#f0f5f5", font=self.fontM))
                self.label[i].grid(row=i, column=0, padx=25, pady=10, sticky="w")
            else:
                self.label.append(ttk.Separator(self.information, orient=HORIZONTAL))
                self.label[i].grid(row=i, column=0, columnspan=2, pady=10, sticky="we")

        self.truck.NewEngine.power_band()
        self.powerBand = PhotoImage(file="res\\power_band\\plot.png")
        self.ImagePowerBand = Label(self.information, image=self.powerBand, bg="#f0f5f5")
        self.ImagePowerBand.grid(row=6, column=1, rowspan=6)
        self.truckColor = Button(self.information, bg=self.truck.get_color(), state=DISABLED, width=30, height=2,
                                 relief=SUNKEN, bd=0)
        self.truckColor.grid(row=len(self.truck.list_result)-2, column=0, sticky="e", padx=150)
        last_row = len(self.truck.list_result)
        self.label2 = []
        for i in range(len(self.truck.list_result1)):
            if self.truck.list_result1[i] != "Separator":
                self.label2.append(Label(self.information, text=self.truck.list_result1[i], bg="#f0f5f5", font=self.fontM))
                self.label2[i].grid(row=last_row+i, column=0, padx=25, pady=10, sticky="w", columnspan=2)
            else:
                self.label2.append(ttk.Separator(self.information, orient=HORIZONTAL))
                self.label2[i].grid(row=last_row+i, column=0, columnspan=2, pady=10, sticky="we")
        self.truck.data.close_connection()
        self.statusBar.config(text="Готово")

    def create_pdf(self):
        CreatePDF(self.truck.list_result, self.truck.list_result1)

# Відкриваємо файл
    def open_file(self):
        try:
            of = askopenfilename(filetypes=[("Data", "*.dat")])
            load_file = open(of, 'rb')
            self.truck = pickle.load(load_file)
            self.load_result()
            load_file.close()
        except:
            pass

    # Закриваємо вайл
    def save_file(self):
        try:
            sf = asksaveasfilename(filetypes=[("Data", "*.dat")])
            save_file = open("{0}.dat".format(sf), 'wb')
            pickle.dump(self.truck, save_file)
            save_file.close()
        except:
            pass

def main():
    root = Tk()
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()
