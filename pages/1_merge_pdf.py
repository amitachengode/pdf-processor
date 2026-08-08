import streamlit as st
from pdf_processor import merge_pdf

if "merged_pdf" not in st.session_state:
    st.session_state.merged_pdf=None

def clear_merge():
    st.session_state.merged_pdf=None

st.set_page_config(page_title="PDF Merger", 
                   page_icon="📄", 
                   layout='wide', 
                   initial_sidebar_state="collapsed")

st.title("PDF Merger")
st.write("Upload multiple PDF files to merge them into one.")

upload_section, export_section = st.columns([3, 1],)

with upload_section:
    st.subheader("Upload")
    uploaded_files = st.file_uploader(label="upload file", 
                                      type=["pdf"], 
                                      accept_multiple_files=True, 
                                      label_visibility="collapsed", 
                                      on_change=clear_merge
                                      )

    if not uploaded_files:
            st.warning("Upload file")

with export_section:
    st.subheader("Export")
    filename = st.text_input("output file name", value="merged_document.pdf")

    is_disabled = not (uploaded_files and len(uploaded_files)>=2)

    if st.button("Merge files", use_container_width=True, disabled=is_disabled):
        with st.spinner():
            st.session_state.merged_pdf = merge_pdf(uploaded_files)
                
    elif len(uploaded_files)<2:
        st.warning("Upload at least two files.")

    if st.session_state.merged_pdf is not None:
        st.download_button("Export", 
                           data=st.session_state.merged_pdf, 
                           file_name=filename, 
                           mime="application/pdf", 
                           use_container_width=True)

