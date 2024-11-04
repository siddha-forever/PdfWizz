import PyPDF2 as pd
import os

import pdfplumber
import pdfplumber as pplum
import fitz #from pymupdf

# Merge PDF
def merge_pdfs(input_folder, output_pdf):
    if os.path.exists(output_pdf):
        os.remove(output_pdf)

    pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]
    pdf_files.sort()

    pdf_writer = pd.PdfWriter()

    for pdf_file in pdf_files:
        with open(os.path.join(input_folder, pdf_file), 'rb') as file:
            pdf_reader = pd.PdfReader(file) 
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                pdf_writer.add_page(page)

    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

# Testing the merge function
# merge_pdfs(input_folder, output_pdf)
# merge_pdf(['Page1.pdf', 'Page2.pdf', 'Page3.pdf', 'Page4.pdf'], 'Merged.pdf')


# Split PDF
def split_pdf(pdf_path, output_dir):
    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    pdf_reader = pd.PdfReader(pdf_path)
    for page_num in range(len(pdf_reader.pages)):
        pdf_writer = pd.PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])
        output_path = f"{output_dir}/page_{page_num + 1}.pdf"

        with open(output_path, 'wb') as out:
            pdf_writer.write(out)

        print(f"SAVED {output_path}")


# Testing the split function
# split_pdf('Merged.pdf', 'Split_Files')

# Extract Text from PDF
def extract_text(pdf_path, output_text_path):
    with pplum.open(pdf_path) as pdf:
        full_text = ''
        for page in pdf.pages:
            full_text += page.extract_text() + '\n'

        with open(output_text_path, 'w') as f:
            f.write(full_text)

        print("Extracted Text!")
        print(f"File saved at {output_text_path}")

# Testing the extract function
# extract_text('Page1.pdf', 'Extracted Text.txt')

# Extract Image from  PDF
import fitz  # PyMuPDF
import os

# Extract Images from PDF
def extract_image(pdf_path, output_dir):
    if not os.path.exists(output_dir): # Create the output directory if it does not exist
        os.makedirs(output_dir)

    pdf_doc = fitz.open(pdf_path)
    for page_num in range(len(pdf_doc)):
        page = pdf_doc.load_page(page_num)
        image_list = page.get_images(full=True)

        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_img = pdf_doc.extract_image(xref)
            img_bytes = base_img["image"]
            img_ext = base_img["ext"]
            img_file_name = f"{output_dir}/image_{page_num+1}_{img_index+1}.{img_ext}"

            with open(img_file_name, 'wb') as img_file:
                img_file.write(img_bytes)

            print(f"Saved {img_file_name}!")

# Testing the extract image function
# extract_image("Page1.pdf", "Extracted_Image")

# Encrypting a pdf file
def encrypt_pdf(input_pdf, output_pdf, password):
    pdf_reader = pd.PdfReader(input_pdf)
    pdf_writer = pd.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    pdf_writer.encrypt(password)

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"File encrypted and Saved as {output_pdf}")

# Testing encryption
# encrypt_pdf("Merged.pdf", "Encrypted.pdf", "123")

# Removing password from PDF
def decrypt_pdf(input_pdf, output_pdf, password):
    pdf_reader = pd.PdfReader(input_pdf)
    pdf_reader.decrypt(password)

    pdf_writer = pd.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"File decryped as {output_pdf}")

# Tesing decryption
# decrypt_pdf("Encrypted.pdf", "Decrypted.pdf", "123")

# Reordering/Rearranging pages in a PDF
def rearrange(input_pdf, output_pdf, page_order):
    pdf_reader = pd.PdfReader(input_pdf)
    pdf_writer = pd.PdfWriter()

    for page_num in page_order:
        pdf_writer.add_page(pdf_reader.pages[page_num])

    with open(output_pdf, 'wb') as out:
        pdf_writer.write(out)

    print(f"File re-arranged as {output_pdf}")

# Tesing rearranged function
# rearrange("Merged.pdf", "changed.pdf", [2,0,1])

# Rotating a page in a PDF
def rotate_page(input_pdf, output_pdf, rotation):
    pdf_reader = pd.PdfReader(input_pdf)
    pdf_writer = pd.PdfWriter()

    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        page.rotate(rotation)
        pdf_writer.add_page(page)

    with open(output_pdf , 'wb') as out:
        pdf_writer.write(out)

    print(f"Orientation has been changed and Saved as {output_pdf}")

# Testing rotated pdf
# rotate_page("Merged.pdf", "Rotate.pdf", 90)

# Compress/Decompress a pdf file
def optimise(input_pdf, output_pdf):
    pdf_doc = fitz.open(input_pdf)
    pdf_doc.save(output_pdf, garbage=3, deflate=True)

    print(f"File has been compressed as {output_pdf}")

# optimise("Merged.pdf", "Compressed.pdf")
