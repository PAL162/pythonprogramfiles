# Generate PDF file of your 3rd Semester Mark sheet
import img2pdf
from PIL import Image
import os
img_path = 'D:sem6result.jpg'
pdf_path = 'D:sem6result.pdf'
image = Image.open(img_path)
pdf_bytes = img2pdf.convert(image.filename)
file = open(pdf_path, "wb")
file.write(pdf_bytes)
image.close()
file.close()
print("successful create pdf file.")
#Khant Pal_D21CE162
