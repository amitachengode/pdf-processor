import streamlit as st
import pypdf
from pdf_processor import drop_pages_pdf, parse_page_ranges

st.set_page_config(page_title="Page Dropper", page_icon="📄", layout='wide')

st.title("Page Dropper")
st.write("Upload a PDF file to drop pages from it.")

uploaded_file = st.file_uploader("Upload PDF file", type=["pdf"], width=400, accept_multiple_files=False)

if uploaded_file:
    
    total_pages = len(pypdf.PdfReader(uploaded_file).pages)
    st.info(f"Document has {total_pages} pages.", width=400)
    
    page_input = st.text_input("Select pages to drop (e.g., 1, 3, 5-10)", placeholder="1, 3, 5-10", width=400)
    
    if st.button("Drop Pages", width=400):
        if not page_input:
            st.warning("Please enter the pages you want to drop.", width=400)
        else:
            with st.spinner("Dropping pages..."):
                
                page_list = parse_page_ranges(page_input, total_pages)
                
                if not page_list:
                    st.error("Invalid format. Please use numbers and dashes (e.g., 1, 3, 5-10).", width=400)
                else:
                    dropped_pdf = drop_pages_pdf(uploaded_file, page_list)
                    
                    st.download_button(
                        label="Download Dropped PDF", 
                        data=dropped_pdf, 
                        file_name="dropped.pdf", 
                        mime="application/pdf",
                        width=400
                    )