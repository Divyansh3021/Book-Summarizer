import index
import PyPDF2, re
import streamlit as st
from flask import Flask, render_template, request

app = Flask(__name__)



@app.route("/get_file", methods = ['GET','POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        return "file uploaded successfully"

@app.route("/read")
def read():
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

    for batch in range(0,(string_len//10)+2):
        for line_index in range(5):
            print(line_index + 5*batch)


    # model_obj = index.summarizer(sub_string)
    # summary += model_obj.summarize(min_length=150)        

    return sub_string



if __name__ == "__main__":
    app.run(debug=False)