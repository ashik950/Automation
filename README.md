# PDF Orientation Correction Script  

## 📌 Overview  
This Python script automatically detects and corrects the orientation of PDF documents using **Tesseract OCR** and **OpenCV**. It processes PDF files in a given directory, adjusts their orientation, and saves the corrected versions.  

## 🚀 Features  
- **Automatic Orientation Detection**: Uses Tesseract OCR to determine the correct orientation of scanned documents.  
- **PDF to Image Conversion**: Converts PDF pages to images using `pdf2image`.  
- **Image Rotation**: Corrects the rotation using OpenCV and `imutils`.  
- **Batch Processing**: Processes all PDFs in the specified input directory.  
- **Saves Corrected PDFs**: Outputs correctly oriented PDFs in the specified folder.  

## 🛠️ Installation  

### **1. Install Dependencies**  
Ensure you have Python installed, then install the required libraries:  
```bash
pip install opencv-python pytesseract pdf2image pillow imutils numpy
