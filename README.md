# Image to PDF - PDF to Image Converter & PDF Merger

This project provides Python scripts for converting images to PDFs, extracting images from PDFs and merging PDFs. It includes multiple methods using different libraries to achieve high-quality conversions.

## Features
- Convert images (`.png`, `.jpg`, etc.) to a PDF.
- Extract images from a PDF and save them as separate image files.
- Merge two or more PDFs.
- Different implementations using **PIL (Pillow)**, **img2pdf**, **PyMuPDF (Fitz)** and **PyPDF2**.
- Supports high-quality output and maintains page order.


## Requirements
Install the required Python packages:
```bash
pip install pillow img2pdf pymupdf PyPDF2
```

## Usage

### 📌 Convert Images to PDF
You can use any of the following methods:

#### ✅ Method 1: Using PIL (Pillow)
Run the following command:
```bash
python img_to_pdf1.py
```

- Drawback: Only works if the folder contains only images (otherwise throws error).

#### ✅ Method 2: Using img2pdf (High DPI)
Run the following command:
```bash
python img_to_pdf2.py
```

- Pros: Maintains high image quality with DPI support.

#### ✅ Method 3: Using PyMuPDF (Fitz) for High-Quality Conversion
Run the following command:
```bash
python img_to_pdf3.py
```

- Pros: Handles different image sizes and maintains full resolution.

### 📌 Convert PDF to Images
Run the following command:
```bash
python pdf_to_img.py
```
- Output: Saves extracted images in the `pdf_images` folder.

### 📌 Merge PDFs
Run the following command:
```bash
python mergePdf.py
```
- Output: Combines/merges PDFs present in the current directory.

## Troubleshooting
- Ensure the images are named properly (e.g., `page_1.png`, `page_2.png`, etc.) to maintain order.
- If running into sorting issues, manually check the filenames before conversion.
- If image quality is low, use **img2pdf** or **PyMuPDF** for better results.

##

### 💡 Suggestions & Contributions are welcome! 🚀