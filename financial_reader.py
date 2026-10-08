import pymupdf

file_name = input("Enter the PDF filename: ")
document = pymupdf.open(file_name)

all_text = ""

for page in document:
    page_text = page.get_text()
    all_text = all_text + page_text + "\n"

lines = all_text.splitlines()
print(lines[:20])

for i, line in enumerate(lines):
    if "Revenue from Operations" in line:
        revenue = lines[i + 2]
        revenue = revenue.replace(" ", "")
        revenue = float(revenue)
        print("REVENUE:", revenue)
        break
for i, line in enumerate(lines):
    if "Total Expenses" in line:
        expense = lines[i+1]   
        expense = expense.replace(" ", "")
        expense = float(expense)
        print("EXPENSE:", expense)
        break
    