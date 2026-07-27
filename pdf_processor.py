import io
import pypdf

def merge_pdf(uploaded_files: list) -> io.BytesIO:
    pdf_writer = pypdf.PdfWriter()

    for file in uploaded_files:
        pdf_reader = pypdf.PdfReader(file)
        pdf_writer.append(pdf_reader)

    output = io.BytesIO()
    pdf_writer.write(output)
    output.seek(0)

    return output

def drop_pages_pdf(uploaded_file: io.BytesIO, page_list: list[int]) -> io.BytesIO:
    pdf_reader = pypdf.PdfReader(uploaded_file)
    pdf_writer = pypdf.PdfWriter()

    for page in pdf_reader.pages:
        if page.page_number not in page_list:
            pdf_writer.add_page(page)

    output = io.BytesIO()
    pdf_writer.write(output)
    output.seek(0)

    return output

def slice_pdf(uploaded_file: io.BytesIO, start_page: int, end_page: int| None = None) -> io.BytesIO:
    pdf_reader = pypdf.PdfReader(uploaded_file)
    pdf_writer = pypdf.PdfWriter()

    for page in pdf_reader.pages[start_page:end_page]:
        pdf_writer.add_page(page)

    output = io.BytesIO()
    pdf_writer.write(output)
    output.seek(0)

    return output