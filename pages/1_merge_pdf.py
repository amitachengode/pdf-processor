import streamlit as st
from pdf_processor import merge_pdf

st.set_page_config(page_title="PDF Merger", page_icon="📄", layout='wide')

st.title("PDF Merger")
st.write("Upload multiple PDF files to merge them into one.")

upload_section, export_section = st.columns([3, 1],)

with upload_section:
    st.subheader("Upload")
    uploaded_files = st.file_uploader(label="", type=["pdf"], accept_multiple_files=True, label_visibility="collapsed")

with export_section:
    st.subheader("Export")
    filename = st.text_input("output file name", value="merged_document.pdf")

    if len(uploaded_files)>=2:
        if st.button("Merge files", use_container_width=True):
            with st.spinner():
                merged_pdf= merge_pdf(uploaded_files)
            st.download_button("Export", data=merged_pdf, file_name=filename, mime="application/pdf", use_container_width=True)
    else:
        st.warning("Upload at least two files.")

