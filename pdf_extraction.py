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
    
    pdf_path = input("Enter your path to your file from root: ")
    try:
        extracted_text = extract_text_from_pdf(pdf_path)
    
        name = pdf_path.split("/")[-1]
        name = name.split(".")[0]
        # Save extracted text to a file
        with open(f"{name}.txt", "w") as output_file:
            output_file.write(extracted_text)

        print(f"Text extraction complete. Check '{name}.txt' for results.")
    except fitz.FileNotFoundError:
        print("Your file name does not exist!")

