# import index
import PyPDF2, re
import streamlit as st
from flask import Flask, render_template, request
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForSeq2SeqLM

app = Flask(__name__)


tokenizer = AutoTokenizer.from_pretrained('t5-small')
model = AutoModelWithLMHead.from_pretrained('t5-small', return_dict = True)
# model = AutoModelForSeq2SeqLM.from_pretrained("sgugger/my-awesome-model")
# model = AutoModelForCausalLM.from_pretrained('t5-small', return_dict = True)


class summarizer:
    
    def summarize(self,text, max_length = 200):
        inputs = tokenizer.encode("summarize: "+text, return_tensors = 'pt', max_length = 1024, truncation = True)
        summarize_ids = model.generate(inputs, max_length = max_length, min_length = 0, length_penalty =3, num_beams = 2)
        summary = tokenizer.decode(summarize_ids[0])
        return summary

    def translate(self):
        inputs = tokenizer.from_pretrained("translate English to German:"+self.text, return_tensors = 'pt', max_length = 1024, truncation = True)
        translation_ids = model.generate(inputs, length_penalty = 4, num_beams = 3)
        translated_text = tokenizer.decode(translation_ids[0])
        return translated_text



@app.route("/")
def read():
    st.title("Book Viewer")

    # Upload PDF book file
    uploaded_file = st.file_uploader("Upload a book file (pdf format)", type=["pdf"])

    # Page navigation
    current_page = st.session_state.get("current_page", 0)
    st.session_state.current_page = current_page

    summarized_text = " "
    summarizer = summarizer()

    # If a file is uploaded
    if uploaded_file is not None:
        st.write("File uploaded successfully.")

        # Display the uploaded book text
        st.subheader("Page {} of the Book:".format(current_page + 1))
        
        if uploaded_file.type == "application/pdf":
            pdf_document = fitz.open(stream=uploaded_file.read())
            num_pages = pdf_document.page_count
            if current_page >= num_pages:
                current_page = num_pages - 1
                st.session_state.current_page = current_page
            
            # Use pdf_document.page_numbers to get the index of the page
            # page_number = pdf_document.page_numbers[current_page]
            
            # Use pdf_document.get_page_text() to get the page text with formatting
            page_text = pdf_document.load_page(current_page).get_text()
            summarized_text += summarizer.summarize(page_text)
            
            # Display the page number and page text
            # st.write(f"Page Number: {page_number}")
            st.markdown(summarized_text, unsafe_allow_html=True)

            # Navigation buttons
            col1, col2, col3 = st.columns(3)
            if col1.button("Previous Page") and current_page > 0:
                st.session_state.current_page -= 1
                summarized_text = " "
            if col3.button("Next Page") and current_page < num_pages - 1:
                st.session_state.current_page += 1
                summarized_text = " "




if __name__ == "__main__":
    app.run(debug=False)