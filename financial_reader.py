import pymupdf
import re

file_name = input("Enter the PDF filename: ")
document = pymupdf.open(file_name)

all_text = ""  #initializing the variable all_text

for page in document:
    page_text = page.get_text()
    all_text = all_text + page_text + "\n"

lines = all_text.splitlines()  #splits text based on starting of new line

for i, line in enumerate(lines):
    if "Revenue from Operations" in line:
        

        for j in range(i + 1, len(lines)):
            value = lines[j]
           

            if re.fullmatch(r"\s*\d[\d, ]*\.\d{2}\s*", value):
                revenue = float(value.replace(" ", "").replace(",", ""))
                
                break
        break
print("REVENUE:", revenue)


for i, line in enumerate(lines):
    if "Total Expenses" in line:
        for j in range(i + 1, len(lines)):
            value = lines[j]

            if re.fullmatch(r"\s*\d[\d, ]*\.\d{2}\s*", value):
                expense = float(value.replace(" ", "").replace(",", ""))
                break
        break

print("EXPENSE:", expense)


profit = round(revenue - expense, 2)
print("PROFIT:", profit)

