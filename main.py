import webbrowser

import fpdf
from fpdf import FPDF

class Bill:
    """
    Object that contains data about the bill, such as total amount and period
    of the bill.
    """

    def __init__(self, amount, period):
        self.period = period
        self.amount = amount


class Flatmate:
    """
    Create a flatmate person who lives in the flat and pays the bill
    """

    def __init__(self, name, days_in_house, ):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay


class PdfReport:
    """
    Create a pdf report that contains data about the flatmates such as their names
    , their due amount and the period of the bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate_pdf(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill,flatmate2),2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        # 'P stands for Portrait mode

        pdf.add_page()

        #add icon
        pdf.image("house.png", w=30 , h=30)

        # Add the title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align="C", ln=1)
        # ln=1 will chnage the line, border=0 will remove the border
        # w=0 will take entire horiziontal length

        #Insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt="Period:", border=1, )
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        #Insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=23, txt=flatmate1.name, border=1, )
        pdf.cell(w=150, h=23, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and due amount of the second flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=23, txt=flatmate2.name, border=1, )
        pdf.cell(w=150, h=23, txt=flatmate2_pay, border=1, ln=1)
        pdf.output(self.filename)
        webbrowser.open(self.filename)


the_bill = Bill(amount=120, period="April 2023")
john = Flatmate(name="John", days_in_house=20)
marry = Flatmate(name="Marry", days_in_house=25)

print("John Pays: ", john.pays(bill=the_bill, flatmate2=marry))

print("Marry Pays: ", marry.pays(bill=the_bill, flatmate2=john))

pdf_report = PdfReport(filename="Report.pdf")
pdf_report.generate_pdf(flatmate1=john, flatmate2=marry, bill=the_bill)