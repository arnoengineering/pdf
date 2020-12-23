import PyPDF2


def read_pdf(file):
    with open(file, 'rb') as pdf:
        pdf_obj = PyPDF2.PdfFileReader(pdf)
    # creating a pdf reader object
    # printing number of pages in pdf file
    page_cnt = pdf_obj.numPages
    print(page_cnt)
    return page_cnt


def reverse(file):
    out_pdf = PyPDF2.PdfFileWriter()
    with open(file, 'rb') as pdf:
        org_pdf = PyPDF2.PdfFileReader(pdf)
        for page in reversed(org_pdf.pages):
            out_pdf.addPage(page)
