# PDF Converter using Docling

This project uses the Docling library to convert PDF documents into different formats, such as text and markdown.

## Requirements

- Python 3.x
- `docling` library

## Installation

1. Clone this repository
2. Install dependencies:

```bash
pip install docling
```

## How to Use

### Convert PDF to Text

```python
from docling.document_converter import DocumentConverter

# PDF document path (local path or URL)
source = "path/to/your/file.pdf"  # or URL

# Initialize converter
converter = DocumentConverter()

# Convert document
result = converter.convert(source)

# Save as text
with open("document_text.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(result.document.export_to_markdown())
```

### Example with URL

```python
from docling.document_converter import DocumentConverter

source = "https://fapes.es.gov.br/Media/fapes/Editais/Edital_01-2025_-_Apoio_%C3%A0s_EJF.pdf"
converter = DocumentConverter()
result = converter.convert(source)

# Save as text
with open("document_text.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(result.document.export_to_markdown())
```

## Supported Formats

- Markdown: `export_to_markdown()`
- Text: You can use markdown or check if your version supports `export_to_text()`

## Tips

- Make sure to use UTF-8 encoding when saving files to preserve special characters
- For URLs with special characters, ensure they are properly encoded

## Troubleshooting

If you encounter errors like "AttributeError", check your Docling library version and consult the documentation for the methods available in the version you're using.
