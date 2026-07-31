import streamlit as st
import pypdf
from pdf_processor import drop_pages_pdf, parse_page_ranges

if "dropped_pdf" not in st.session_state:
    st.session_state.dropped_pdf=None

def clear_drop_state():
    st.session_state.dropped_pdf=None

st.set_page_config(page_title="Page Dropper", page_icon="📄", layout='wide')

st.title("Page Dropper")
st.write("Upload a PDF file to drop pages from it.")

upload_section, export_section = st.columns([3, 1],)

with upload_section:
    st.subheader("Upload")
    uploaded_files = st.file_uploader(label="", type=["pdf"], accept_multiple_files=False, label_visibility="collapsed", on_change=clear_drop_state)

    if not uploaded_files:
            st.warning("Upload file")

with export_section:
    st.subheader("Export")
    page_input = st.text_input("Select pages to drop (e.g., 1, 3, 5-10)", placeholder="1, 3, 5-10", on_change=clear_drop_state)
    filename = st.text_input("output file name", value="dropped_document.pdf")

    is_disabled = not (uploaded_files and page_input)

    if st.button("Drop page", use_container_width=True, disabled=is_disabled):
        with st.spinner():
            total_pages = len(pypdf.PdfReader(uploaded_files).pages)
            page_list = parse_page_ranges(page_input, total_pages)
            st.session_state.dropped_pdf = drop_pages_pdf(uploaded_files, page_list)

    elif uploaded_files and not page_input:
        st.warning("Enter the range in proper format.")

    if st.session_state.dropped_pdf:
        st.download_button(label="Export", data=st.session_state.dropped_pdf, file_name=filename, mime="application/pdf", use_container_width=True)