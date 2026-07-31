import streamlit as st
import pypdf
from pdf_processor import slice_pdf

if "sliced_pdf" not in st.session_state:
    st.session_state.sliced_pdf=None

def clear_sliced_state():
    st.session_state.sliced_pdf=None

st.set_page_config(page_title="PDF Spliter", 
                   page_icon="📄", 
                   layout='wide', 
                   initial_sidebar_state="collapsed"
                   )

st.title("PDF Slicer")
st.write("Upload a PDF file to slice it portion of the pdf.")

upload_section, export_section = st.columns([3, 1],)

with upload_section:
    st.subheader("Upload")
    uploaded_files = st.file_uploader(label="", 
                                      type=["pdf"], 
                                      accept_multiple_files=False, 
                                      label_visibility="collapsed", 
                                      on_change=clear_sliced_state
                                      )

    if not uploaded_files:
        st.warning("Upload file")
    else:
        pages_len = len(pypdf.PdfReader(uploaded_files).pages)
        st.write(f"Page count: {pages_len}")

with export_section:
    st.subheader("Export")
    start_page = st.number_input("Start Page", 
                                 min_value=1, 
                                 max_value=None, 
                                 value=1, 
                                 on_change=clear_sliced_state
                                 )
    end_page = st.number_input("End Page", 
                               min_value=1, 
                               max_value=None, 
                               value=None, 
                               on_change=clear_sliced_state)
    filename = st.text_input("output file name", value="sliced_document.pdf")

    is_disabled = not uploaded_files

    if st.button("Split", 
                 use_container_width=True, 
                 disabled=is_disabled):
        with st.spinner():
            st.session_state.sliced_pdf = slice_pdf(uploaded_files, 
                                                    start_page-1, 
                                                    end_page=end_page if end_page else None
                                                    )

    if st.session_state.sliced_pdf:
        st.download_button("Export", 
                           data=st.session_state.sliced_pdf, 
                           file_name=filename, mime="application/pdf", 
                           use_container_width=True)