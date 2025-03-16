import fitz  # PyMuPDF
import os

# Replace with your folder path
directory_path = r"D:\My Projects\Img_To_Pdf Converter\pdf_images"

# Output PDF file
output_pdf_path = os.path.join(directory_path, "output.pdf")

# Create a new PDF document
pdf_document = fitz.open()

# Get sorted image files
image_files = sorted(
    [i for i in os.listdir(directory_path) if i.endswith(".png")],
    key=lambda x: int(os.path.splitext(x)[0].split('_')[-1])  # Sort the pages numerically
)

# Loop through sorted images and add to PDF
for img_file in image_files:
    img_path = os.path.join(directory_path, img_file)

    # Load image and get dimensions
    img = fitz.open(img_path)
    rect = img[0].rect  # Get image size

    # Create a new blank page and insert the image
    page = pdf_document.new_page(width=rect.width, height=rect.height)
    page.insert_image(rect, filename=img_path)

# Save PDF
pdf_document.save(output_pdf_path)
pdf_document.close()

print(f"Your PDF is saved at: {output_pdf_path}")
