# import streamlit as st
# import requests
# import PyPDF2

# # Set up the Streamlit app
# st.title("Book Summarizer")

# # Upload PDF book file
# uploaded_file = st.file_uploader("Upload a book file (pdf format)", type=["pdf"])

# # If a file is uploaded
# if uploaded_file is not None:
#     st.write("File uploaded successfully.")

#     # Display the uploaded book text
#     st.subheader("Uploaded Book Text:")
#     if uploaded_file.type == "application/pdf":
#         pdf_reader = PyPDF2.PdfReader(uploaded_file)
#         pdf_text = ""
#         for page_num in range(len(pdf_reader.pages)):
#             page = pdf_reader.pages[page_num]
#             pdf_text += page.extract_text()
#         st.write(pdf_text)

#         # Summarize the book
#         if st.button("Summarize"):
#             # Send the PDF text to the backend for summarization
#             backend_url = "http://your-backend-url/summarize"  # Replace with your actual backend URL
#             response = requests.post(backend_url, data=pdf_text)

#             if response.status_code == 200:
#                 summarized_text = response.text
#                 st.subheader("Summarized Book:")
#                 st.write(summarized_text)
#             else:
#                 st.error("An error occurred during summarization. Please try again.")
#     else:
#         st.error("Please upload a PDF file.")

import streamlit as st
from pdf2image import convert_from_bytes
from PIL import Image

# Set up the Streamlit app
st.title("Book Viewer")

# Upload PDF book file
uploaded_file = st.file_uploader("Upload a book file (pdf format)", type=["pdf"])

# Page navigation
current_page = st.session_state.get("current_page", 0)
st.session_state.current_page = current_page

# If a file is uploaded
if uploaded_file is not None:
    st.write("File uploaded successfully.")

    # Display the uploaded book text
    st.subheader("Page {} of the Book:".format(current_page + 1))

    page_text = ""

    # Create a fixed-height container for displaying the text
    text_container = st.empty()

    if uploaded_file.type == "application/pdf":
        pdf_bytes = uploaded_file.read()
        pdf_images = convert_from_bytes(pdf_bytes)
        num_pages = len(pdf_images)
        if current_page >= num_pages:
            current_page = num_pages - 1
            st.session_state.current_page = current_page

        image = pdf_images[current_page]
        st.image(image, caption=f"Page {current_page + 1}", use_column_width=True)
        
        # Navigation buttons
        col1, col2, col3 = st.columns(3)
        if col1.button("Previous Page") and current_page > 0:
            st.session_state.current_page -= 1
        if col3.button("Next Page") and current_page < num_pages - 1:
            st.session_state.current_page += 1

