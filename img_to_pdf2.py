import os
import img2pdf

# Replace with your actual folder path
directory_path = r"D:\My Projects\Img_To_Pdf Converter\pdf_images"

# Get full file paths for all PNG images and sort them numerically
image_files = sorted(
    [os.path.join(directory_path, i) for i in os.listdir(directory_path) if i.endswith(".png")],
    key=lambda x: int(os.path.splitext(os.path.basename(x))[0].split('_')[-1])  # Sort the pages by numeric index
)

# Convert images to PDF with high DPI
pdf_data = img2pdf.convert(image_files, dpi=300)

# Save the PDF
output_pdf_path = os.path.join(directory_path, "output.pdf")
with open(output_pdf_path, "wb") as file:
    file.write(pdf_data)

print(f"Your PDF is saved at: {output_pdf_path}")
