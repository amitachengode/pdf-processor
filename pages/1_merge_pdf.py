import streamlit as st
from pdf_processor import merge_pdf


st.set_page_config(page_title="PDF Merger", page_icon="📄", layout='wide')

st.title("PDF Merger")
st.write("Upload multiple PDF files to merge them into one.")

upload_section, download_section = st.columns(2,)

uploaded_files = st.file_uploader("Upload PDF files", type=["pdf"], accept_multiple_files=True, width=400)

if uploaded_files:
    if st.button("Merge PDFs", width=400):

        with st.spinner("Merging PDFs..."):
            merged_pdf = merge_pdf(uploaded_files)
            
        st.download_button("Download Merged PDF", merged_pdf, "merged.pdf", "application/pdf", width=400)