import PyPDF2
import re

pdfFileObject = open("D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf", 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObject)
lines = []
string = ""
#Storing the pages in a list
for i in range(8,18):
    pageObj = pdfReader.pages[i].extract_text()

    lines.extend(line.strip().replace('\t', ' ') for line in pageObj.split('\n') if line.strip())

    for line in lines:
        string += line

print(string)