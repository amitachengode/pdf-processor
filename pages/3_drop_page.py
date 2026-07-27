import streamlit as st
import pypdf
from pdf_processor import drop_pages_pdf

# --- 1. The Parser Function ---
def parse_page_ranges(range_string: str, max_pages: int) -> list[int]:
    pages_to_drop = set()
    
    for part in range_string.split(','):
        part = part.strip()
        if not part:
            continue
            
        if '-' in part:
            try:
                start, end = map(int, part.split('-'))
                start = max(1, start)
                end = min(max_pages, end)
                if start <= end:
                    for p in range(start, end + 1):
                        pages_to_drop.add(p - 1)
            except ValueError:
                pass                
        else:
            try:
                p = int(part)
                if 1 <= p <= max_pages:
                    pages_to_drop.add(p - 1)
            except ValueError:
                pass
                
    return list(pages_to_drop)

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