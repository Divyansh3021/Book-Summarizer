import re, PyPDF2

def extract_text_pypdf2(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        # num_pages = reader.numPages
        text = ''
        for page_num in range(5,20):
            page = reader.pages[page_num]
            page_text = page.extract_text()
            # Filter out common patterns like page numbers
            # filtered_text = re.sub(r'\b\d+\b', '', page_text)
            text += page_text
        return text

text = extract_text_pypdf2("D:\Books\Atomic Habits An Easy  Proven Way to Build Good Habits  Break Bad Ones (James Clear).pdf")
print(text)