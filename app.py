import streamlit as st

st.set_page_config(
    page_title="PDF Toolkit",
    page_icon="📄",
    layout="centered"
)

st.title("Welcome to the PDF Toolkit")
st.markdown("#### Fast, secure, and fully in-memory PDF manipulation.")

st.write(
    "Whether you need to combine monthly reports, extract a specific chapter, "
    "or clean up a scanned document by removing blank pages, this toolkit handles it instantly. "
    "Because everything is processed directly in memory using Python, your sensitive documents "
    "never touch a hard drive—ensuring **100% privacy** and zero leftover files."
)

st.write("---")

st.write("### Available Tools:")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("**Merge PDFs**\n\nCombine two or more PDF files into a single, continuous document.")
    if st.button("Launch", key="merge_btn", use_container_width=True):
        st.switch_page("pages/1_merge_pdf.py")

with col2:
    st.info("**Slice PDF**\n\nExtract a specific range of pages (e.g., pages 5 through 10) into a new file.")

with col3:
    st.info("**Drop Pages**\n\nRemove specific, individual pages from a document to clean it up.")

st.write("---")