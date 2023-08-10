import PyPDF2
import re

import index

pdfFileObject = open("D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf", 'rb')
# creating a pdf reader object
pdfReader = PyPDF2.PdfReader(pdfFileObject)
lines = []
string = ""
summary = ""
#Storing the pages in a list
for i in range(8,10):
    pageObj = pdfReader.pages[i].extract_text()
    lines.extend(line.strip().replace('\t', ' ') for line in pageObj.split('\n') if line.strip())
    for line in lines:
        string += line


string = string.split(".")

sub_string = ""

string_len = len(string)

print("Length of string is : ",string_len)

for batch in range(0,(string_len//15)+1):
    for line_index in range(15):
        sub_string += string[line_index + 15*batch] + "."

    model_obj = index.summarizer(sub_string)
    summary = model_obj.summarize(max_length=20, min_length=10)

    print(summary)
    sub_string = ""

