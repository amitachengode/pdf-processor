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