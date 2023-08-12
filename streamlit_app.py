import streamlit as st
import fitz  # PyMuPDF
import index

# Set up the Streamlit app
st.title("Book Viewer")

# Upload PDF book file
uploaded_file = st.file_uploader("Upload a book file (pdf format)", type=["pdf"])

# Page navigation
current_page = st.session_state.get("current_page", 0)
st.session_state.current_page = current_page

summarized_text = " "
summarizer = index.summarizer()

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
