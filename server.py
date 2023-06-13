import index
import PyPDF2, re
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def upload():
    return render_template("home.html")

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

    sub_string = []
    empty_string = ""


    string = string.split()
    print(string)




    # model_obj = index.summarizer(string)
    # summary += model_obj.summarize(min_length=150)        

    return summary



if __name__ == "__main__":
    app.run(debug=True)