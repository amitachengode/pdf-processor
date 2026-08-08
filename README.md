# PDF Toolkit

A fast, secure, and privacy-focused PDF manipulation application built with Streamlit. Process your PDFs entirely in memory with zero leftover files on disk.

Visit [pdfisbeingprocessed.streamlit.app](https://pdfisbeingprocessed.streamlit.app/)

## Features

### Merge PDFs

Combine two or more PDF files into a single, continuous document. Perfect for consolidating reports, invoices, or multi-part documents.

### Slice PDF

Extract a specific range of pages (e.g., pages 5 through 10) from a PDF. Useful for isolating chapters, sections, or specific content from larger documents.

### Drop Pages

Remove specific individual pages from a document. Use flexible syntax to drop single pages or page ranges (e.g., `1, 3, 5-10`).

## Security & Privacy

- **In-memory processing**: All PDF operations happen in RAM—documents never touch your hard drive
- **100% private**: No files are saved to disk between operations
- **No tracking**: Everything is processed locally in your browser session
- **Secure**: Uses industry-standard PyPDF library for reliable PDF manipulation

## Quick Start

### Prerequisites

- Python 3.14 or higher
- pip or uv package manager

### Installation

1. Clone the repository:

```bash
git clone https://github.com/amitachengode/pdf-processor.git
cd pdf-processor
```

2. Install dependencies:

```bash
# Using uv (recommended)
uv sync

# OR using pip
pip install -r requirements.txt
```

### Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage

### Home Page

The main dashboard displays all three tools with quick-access buttons to launch each feature.

### Merge PDFs

1. Navigate to the **Merge PDFs** tool
2. Click "Upload PDF files" to select multiple files
3. Click **Merge PDFs** button
4. Download your merged document

### Slice PDF

1. Navigate to the **Slice PDF** tool
2. Upload a PDF file
3. Enter the starting page number (1-indexed)
4. (Optional) Enter the ending page number to define your range
5. Click **Slice PDF** button
6. Download your sliced document

### Drop Pages

1. Navigate to the **Drop Pages** tool
2. Upload a PDF file (the app shows total page count)
3. Enter pages to remove using flexible syntax:
   - Single pages: `1, 3, 5`
   - Page ranges: `5-10` (drops pages 5 through 10)
   - Mixed: `1, 3, 5-10` (drops pages 1, 3, and 5-10)
4. Click **Drop Pages** button
5. Download your modified document

## Project Structure

```
pdf-processor/
├── app.py                    # Main Streamlit app entry point
├── pdf_processor.py          # Core PDF manipulation functions
├── pyproject.toml            # Project metadata and dependencies
└── pages/
    ├── 1_merge_pdf.py       # PDF merge tool UI
    ├── 2_slice_pdf.py       # PDF slicer UI
    └── 3_drop_page.py       # Page dropper UI
```

## Dependencies

- **streamlit** (>=1.60.0) - Web app framework
- **pypdf** (>=6.14.2) - PDF manipulation library

See `pyproject.toml` for complete dependency specifications.

## Future Enhancements

Potential features for future releases:

- Rotate pages
- Reorder pages
- Add watermarks
- Compress PDFs
- Extract text/images
- Split PDF by bookmarks
