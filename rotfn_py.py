import os
import cv2
import pytesseract
from pytesseract import Output
from pdf2image import convert_from_path
from PIL import Image
import imutils
import numpy as np

# Configure Tesseract executable and tessdata path
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\BIZZJMC - 151\Downloads\Tesseract-OCR\Tesseract-OCR\tesseract.exe"
#os.environ["TESSDATA_PREFIX"] = r"C:\Users\BIZZJMC - 151\Downloads\Tesseract-OCR\Tesseract-OCR\tessdata"

# Define input and output directories
input_dir = "D:/Files"
output_dir = "D:/rotate_correct/output"

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

def correct_orientation(image):
    """Correct the orientation of an image using Tesseract."""
    rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = pytesseract.image_to_osd(rgb, output_type=Output.DICT)
    rotate_angle = results.get("rotate", 0)
    print(f"[INFO] Detected orientation: {results['orientation']}")
    print(f"[INFO] Rotate by {rotate_angle} degrees to correct.")
    # Rotate the image to the correct orientation
    corrected_image = imutils.rotate_bound(image, angle=rotate_angle)
    return corrected_image

def process_pdf(input_path, output_path):
    """Process a PDF file, correct orientation, and save as a corrected PDF."""
    # Convert PDF pages to images
    images = convert_from_path(input_path)
    corrected_pages = []
    for page_image in images:
        # Convert the PIL image to OpenCV format
        page_array = cv2.cvtColor(np.array(page_image), cv2.COLOR_RGB2BGR)
        # Correct orientation
        corrected_image = correct_orientation(page_array)
        # Convert back to PIL format
        corrected_pages.append(Image.fromarray(cv2.cvtColor(corrected_image, cv2.COLOR_BGR2RGB)))
    # Save all corrected pages into a single PDF
    corrected_pdf_path = os.path.join(output_path, f"{os.path.splitext(os.path.basename(input_path))[0]}_corrected.pdf")
    corrected_pages[0].save(corrected_pdf_path, save_all=True, append_images=corrected_pages[1:])
    print(f"[INFO] Saved corrected PDF: {corrected_pdf_path}")

def main():
    # Iterate through all PDF files in the input directory
    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            print(f"Processing: {input_path}")
            # Create the output directory for corrected PDFs
            os.makedirs(output_dir, exist_ok=True)
            process_pdf(input_path, output_dir)
    print("Processing complete.")

if __name__ == "__main__":
    main()
