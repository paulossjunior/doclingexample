from docling.document_converter import DocumentConverter
import os
import time

# List of PDF documents (URLs or local paths)
edital_sources = [
    "https://fapes.es.gov.br/Media/fapes/Editais/Edital_01-2025_-_Apoio_%C3%A0s_EJF.pdf",
    "https://fapes.es.gov.br/Media/fapes/Editais/Edital_04-2025_-_Universal_Extens%C3%A3o.pdf"     # Add more URLs or file paths here
]

# Initialize converter
converter = DocumentConverter()

# Create output directory if it doesn't exist
output_dir = "converted_editais"
os.makedirs(output_dir, exist_ok=True)

# Process each document in the list
for index, source in enumerate(edital_sources):
    try:
        print(f"Converting document {index+1}/{len(edital_sources)}: {source}")
        
        # Extract filename from URL or path
        if source.startswith("http"):
            filename = source.split("/")[-1].split("?")[0]  # Handle URLs with query parameters
        else:
            filename = os.path.basename(source)
            
        # Clean up filename
        filename = filename.replace("%", "").replace("_", "-")
        base_filename = os.path.splitext(filename)[0]
        
        # Convert document
        result = converter.convert(source)
        
        # Save as text file
        text_path = os.path.join(output_dir, f"{base_filename}.txt")
        with open(text_path, "w", encoding="utf-8") as txt_file:
            txt_file.write(result.document.export_to_markdown())
            
        print(f"✓ Saved to {text_path}")
        
        # Optional: Add a small delay between requests to avoid overwhelming the server
        if index < len(edital_sources) - 1:
            time.sleep(2)
            
    except Exception as e:
        print(f"❌ Error processing {source}: {str(e)}")

print(f"\nConversion complete. {len(edital_sources)} documents processed.")
print(f"Files saved to the '{output_dir}' directory.")
