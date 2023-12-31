from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv", sep=",")

for index, row in df.iterrows():
    for i in range(row['Pages']):
        pdf.add_page()

        # Set the header
        pdf.set_font(family="Times", style="B", size=24)
        pdf.set_text_color(100, 100, 100)  # gray color
        pdf.cell(w=0, h=12, txt=row['Topic'], align="L", ln=1)

        # Add multiple lines with height 10mm distance
        pdf.set_text_color(0, 0, 100)  # blue color
        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # line break
        pdf.ln(265)

        # Set the footer
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align="R")

pdf.output("output.pdf")
