import pymupdf
import re

file_name = input("Enter the PDF filename: ")
try:
    document = pymupdf.open(file_name)
except pymupdf.FileNotFoundError:
    print("Error: PDF file not found!")
    exit()
except pymupdf.FileDataError:
    print("Error: The file is not a valid PDF.")
    exit()   

if not document.is_pdf:
    print("Error: The file is not a valid PDF.")
    exit()     

all_text = ""  #initializing the variable all_text

for page in document:
    page_text = page.get_text()
    all_text = all_text + page_text + "\n"

document.close()    

lines = all_text.splitlines()  #splits text based on 
revenue = None
expense = None

# Revenue Block
for i, line in enumerate(lines):
    if "Revenue from Operations" in line:
        for j in range(i + 1, len(lines)):
            value = lines[j]
            if re.fullmatch(r"\s*\d[\d, ]*\.\d{2}\s*", value):
                revenue = float(value.replace(" ", "").replace(",", ""))
                break
        break


# Expense Block
for i, line in enumerate(lines):
    if "Total Expenses" in line:
        for j in range(i + 1, len(lines)):
            value = lines[j]
            if re.fullmatch(r"\s*\d[\d, ]*\.\d{2}\s*", value):
                expense = float(value.replace(" ", "").replace(",", ""))
                break
        break


if revenue is None or expense is None:
    print("Error: Revenue or expenses not found in PDF.")
    exit()

print("REVENUE:", revenue)
print("EXPENSE:", expense)

profit = round(revenue - expense, 2)
print("PROFIT:", profit)

