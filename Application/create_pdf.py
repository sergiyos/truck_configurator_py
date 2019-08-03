from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from tkinter.filedialog import asksaveasfilename


class CreatePDF:

    def __init__(self, list1, list2):
        step = 800
        c = canvas.Canvas("%s.pdf" % asksaveasfilename(filetypes=[("Document", "*.pdf")]), pagesize=A4)
        pdfmetrics.registerFont(TTFont('Verdana', 'font\\Verdana.ttf'))
        c.setFont('Verdana', 10)

        for i in range(len(list1)):
            if list1[i] != "Separator":
                c.drawString(50, step, list1[i])
                step -= 15
            else:
                c.line(50, step, 525, step)
                step -= 15

        for i in range(len(list2)):
            if i == 2 :
                c.drawString(50, step, list2[i][:70])
                step -= 15
                c.drawString(50, step, list2[i][71:])
                step -= 15
                print(list2[i][:70])
                print(list2[i][71:])

            if list2[i] != "Separator":
                if i != 2:
                    c.drawString(50, step, list2[i])
                    step -= 15
            else:
                c.line(50, step, 525, step)
                step -= 15
        c.save()




