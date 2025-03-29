from docling.document_converter import DocumentConverter

# Caminho do documento PDF (URL ou caminho local)
source = "https://fapes.es.gov.br/Media/fapes/Editais/Edital_01-2025_-_Apoio_%C3%A0s_EJF.pdf"

# Inicializar o conversor
converter = DocumentConverter()

# Converter o documento
result = converter.convert(source)

# Obter o conteúdo em markdown
markdown_text = result.document.export_to_markdown()

# Salvar o conteúdo como texto simples UTF-8
with open("documento_texto.txt", "w", encoding="utf-8") as txt_file:
    txt_file.write(markdown_text)

print("Documento convertido e salvo como 'documento_texto.txt' em formato de texto UTF-8")
