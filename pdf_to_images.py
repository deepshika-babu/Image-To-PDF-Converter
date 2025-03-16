import fitz  # PyMuPDF
import os

# PDF file path
pdf_path = r"D:\My Projects\Img_To_Pdf Converter\Sample-pdf.pdf"

# Output folder for images
output_folder = r"D:\My Projects\Img_To_Pdf Converter\pdf_images"
os.makedirs(output_folder, exist_ok=True)

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Loop through each page and save as an image
for page_number in range(len(pdf_document)):
    page = pdf_document.load_page(page_number)  # Load page
    image = page.get_pixmap()  # Render page as an image
    img_path = os.path.join(output_folder, f"page_{page_number+1}.png")
    
    # Save image
    image.save(img_path)

print(f"PDF converted to images in {output_folder}")