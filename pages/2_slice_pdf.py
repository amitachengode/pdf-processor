import streamlit as st
from pdf_processor import slice_pdf

st.set_page_config(page_title="PDF Spliter", page_icon="📄", layout='wide')

st.title("PDF Slicer")
st.write("Upload a PDF file to slice it portion of the pdf.")

uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"], width=400)

if uploaded_file:
    start_page = st.number_input("Start Page", min_value=1, max_value=None, value=1, width=400)
    end_page = st.number_input("End Page", min_value=1, max_value=None, value=None, width=400)

    if st.button("Slice PDF", width=400):

        with st.spinner("Slicing PDF..."):
            sliced_pdf = slice_pdf(uploaded_file, start_page-1, end_page if end_page else None)
            
        st.download_button("Download Sliced PDF", sliced_pdf, "sliced.pdf", "application/pdf", width=400)