import os
from datetime import datetime
import pypdf

def merge_pdf(*pdf_list: str) -> str:
    os.makedirs("temp", exist_ok=True)

    pdf_writer = pypdf.PdfWriter()
    for pdf_path in pdf_list:
        pdf_writer.append(pdf_path)
    output_path = f"temp/merged_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    with open(output_path, "wb") as f:
        pdf_writer.write(f)

    return output_path

def drop_pages_pdf(pdf_path: str, page_list: list[int]) -> str:
    os.makedirs("temp", exist_ok=True)

    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    page_set = set(page_list)
    for index, pages in enumerate(pdf_reader.pages):
        if index not in page_set:
            pdf_writer.add_page(pages)

    output_path = f"temp/dropped_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    with open(output_path, "wb") as f:
        pdf_writer.write(f)

    return output_path

def slice_pdf(pdf_path: str, start_page: int, end_page: int| None = None) -> str:
    os.makedirs("temp", exist_ok=True)

    pdf_reader = pypdf.PdfReader(pdf_path)
    pdf_writer = pypdf.PdfWriter()

    for page in pdf_reader.pages[start_page:end_page]:
        pdf_writer.add_page(page)

    output_path = f"temp/sliced_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.pdf"
    with open(output_path, "wb") as f:
        pdf_writer.write(f)

    return output_path