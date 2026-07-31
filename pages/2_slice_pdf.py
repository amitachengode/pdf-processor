import streamlit as st
import pypdf
from pdf_processor import slice_pdf

st.set_page_config(page_title="PDF Spliter", page_icon="📄", layout='wide')

st.title("PDF Slicer")
st.write("Upload a PDF file to slice it portion of the pdf.")

upload_section, export_section = st.columns([3, 1],)

with upload_section:
    st.subheader("Upload")
    uploaded_files = st.file_uploader(label="", type=["pdf"], accept_multiple_files=False, label_visibility="collapsed")

    if not uploaded_files:
        st.warning("Upload file for slicing.")
    else:
        pages_len = len(pypdf.PdfReader(uploaded_files).pages)
        st.write(f"Page count: {pages_len}")

with export_section:
    st.subheader("Export")
    start_page = st.number_input("Start Page", min_value=1, max_value=None, value=1)
    end_page = st.number_input("End Page", min_value=1, max_value=None, value=None)
    filename = st.text_input("output file name", value="sliced_document.pdf")

    if uploaded_files:
        if st.button("Split", use_container_width=True):
            with st.spinner():
                sliced_pdf = slice_pdf(uploaded_files, start_page-1, end_page=end_page if end_page else None)
            st.download_button("Download Sliced PDF", data=sliced_pdf, file_name=filename, mime="application/pdf", use_container_width=True)

    else:
        st.button("Split", use_container_width=True, disabled=True)