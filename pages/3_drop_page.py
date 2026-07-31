import streamlit as st
import pypdf
from pdf_processor import drop_pages_pdf, parse_page_ranges

st.set_page_config(page_title="Page Dropper", page_icon="📄", layout='wide')

st.title("Page Dropper")
st.write("Upload a PDF file to drop pages from it.")

upload_section, export_section = st.columns([3, 1],)

with upload_section:
    st.subheader("Upload")
    uploaded_files = st.file_uploader(label="", type=["pdf"], accept_multiple_files=False, label_visibility="collapsed")

with export_section:
    st.subheader("Export")
    page_input = st.text_input("Select pages to drop (e.g., 1, 3, 5-10)", placeholder="1, 3, 5-10")
    filename = st.text_input("output file name", value="dropped_document.pdf")
    if page_input:
        if st.button("Drop page", use_container_width=True):
            with st.spinner():
                total_pages = len(pypdf.PdfReader(uploaded_files).pages)
                page_list = parse_page_ranges(page_input, total_pages)
                dropped_pdf = drop_pages_pdf(uploaded_files, page_list)
            st.download_button(label="Export", data=dropped_pdf, file_name=filename, mime="application/pdf", use_container_width=True)
    else:
        st.warning("Enter the range in proper format.")