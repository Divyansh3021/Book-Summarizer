# import re, PyPDF2

# def extract_text_pypdf2(file_path):
#     with open(file_path, 'rb') as file:
#         reader = PyPDF2.PdfReader(file)
#         # num_pages = reader.numPages
#         text = ''
#         for page_num in range(5,20):
#             page = reader.pages[page_num]
#             page_text = page.extract_text()
#             page_text = page_text.replace('\t\r', " ")
#             page_text = page_text.replace("\xa0", " ")
#             # Filter out common patterns like page numbers
#             # filtered_text = re.sub(r'\b\d+\b', '', page_text)
#             text += page_text
#         return text

# creating a pdf file object
# pdfFileObject = open("D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf", 'rb')
# # creating a pdf reader object
# pdfReader = PyPDF2.PdfReader(pdfFileObject)
# text=""
# summary=' '
# #Storing the pages in a list
# for i in range(0,len(pdfReader.pages)):
#   # creating a page object
#   pageObj = pdfReader.pages[i].extract_text()
#   pageObj= pageObj.replace('/t/r',' ')
#   pageObj= pageObj.replace('/xa0',' ')
#   # extracting text from page
#   text += pageObj

# # text = extract_text_pypdf2("D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf")
# print(text)

# import PyPDF2
# import re

# def extract_headings_from_pdf(pdf_path):
#     # Open the PDF file
#     with open("D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf", 'rb') as file:
#         # Initialize a PDF reader object
#         reader = PyPDF2.PdfReader(file)
        
#         # Initialize an empty list to store the headings
#         headings = []
        
#         # Iterate over each page in the PDF
#         for page_num in range(7,18):
#             # Extract the text from the page
#             page = reader.pages[page_num]
#             text = page.extract_text()
            
#             # Split the text into paragraphs
#             paragraphs = text.split('\n\n')
            
#             # Regular expression pattern to match headings in all capital letters
#             pattern = r'^[A-Z\s]+$'
            
#             # Iterate over each paragraph
#             for paragraph in paragraphs:
#                 # Remove any leading or trailing whitespaces from the paragraph
#                 paragraph = paragraph.strip()
#                 print(paragraph)
                
#                 # Check if the paragraph matches the pattern of a heading
#                 if re.match(pattern, paragraph):
#                     headings.append(paragraph)
    
#     return headings

# # Example usage
# pdf_path = '"D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf"'
# extracted_headings = extract_headings_from_pdf(pdf_path)
# print(extracted_headings)


import fitz
import re

def extract_headings_from_pdf(pdf_path):
    headings = []
    
    # Open the PDF file
    with fitz.open(pdf_path) as doc:
        # Iterate over each page in the PDF
        for page in doc:
            # Extract the text from the page
            text = page.get_text()
            
            # Split the text into paragraphs
            paragraphs = text.split('\n\n')
            
            # Regular expression pattern to match headings in all capital letters
            pattern = r'^[A-Z\s]+$'
            
            # Iterate over each paragraph
            for paragraph in paragraphs:
                # Remove any leading or trailing whitespaces from the paragraph
                paragraph = paragraph.strip()
                
                # Check if the paragraph matches the pattern of a heading
                if re.match(pattern, paragraph):
                    headings.append(paragraph)
    
    return headings

# Example usage
pdf_path = 'path/to/your/pdf/file.pdf'
extracted_headings = extract_headings_from_pdf(pdf_path)
print(extracted_headings)
