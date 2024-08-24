import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    # Open the PDF file
    doc = fitz.open(pdf_path)
    all_text = ""

    # Iterate through each page
    for page_num in range(len(doc)):
        # Extract text from each page
        page = doc.load_page(page_num)  # Page number starts from 0
        text = page.get_text("text")  # Use "text" to extract raw text
        all_text += text + "\n"  # Add a newline after each page

    doc.close()  # Close the document
    return all_text

if __name__ == "__main__":
    pdf_path = "/Users/robertrzhang/Downloads/Med-School-Acceptance-Stats-2023.pdf"
    extracted_text = extract_text_from_pdf(pdf_path)
    
    # Save extracted text to a file
    with open("output.txt", "w") as output_file:
        output_file.write(extracted_text)

    print("Text extraction complete. Check 'output.txt' for results.")
