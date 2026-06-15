import fitz

def sign_pdf(pdf_path, signature_path, output_path):

    pdf = fitz.open(pdf_path)

    page = pdf[0]

    rect = fitz.Rect(
    100, 230,
    420, 500
)
    page.insert_image(
        rect,
        filename=signature_path
    )

    pdf.save(output_path)
    pdf.close()