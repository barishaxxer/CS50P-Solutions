from fpdf import FPDF

name = input("Name: ")

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
pdf.set_font("helvetica", "B", 16)
pdf.image("shirtificate.png", 50, 45, 110, 207)
pdf.cell(0, 0, "CS50 Shirtificate", border=0, align="C", fill=False, link="")
pdf.set_text_color(255, 255, 255)

pdf.cell(-190, 160, f"{name} took CS50", align="C")

pdf.output("shirtificate.pdf")
