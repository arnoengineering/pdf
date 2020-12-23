import PyPDF2
import os

# find files path/class/(f,b)
path = ''
dirs = os.listdir(path)

for di in dirs:
    files = os.listdir(os.path.join(path, di))
    pdf_objs = []
    output_file = files[0] + '-output'  # TODO before .pdf
    out_pdf = PyPDF2.PdfFileWriter()

    # todo find all files
    for fi in files:
        with open(fi, 'rb') as pdf:
            pdf_objs.append(PyPDF2.PdfFileReader(pdf))

    nums = [o.numPages() for o in pdf_objs]
    min_len = min(nums)
    max_len = max(nums)
    max_in = nums.index(max_len)

    # todo fix so other one is added completely
    for x in range(min_len):
        out_pdf.addPage(pdf_objs[0].getPage(x))
        out_pdf.addPage(pdf_objs[1].getPage(-(x + 1)))

    if max_in == 0:
        for x in range(min_len, max_len):  # todo fix so Index correct
            out_pdf.addPage(pdf_objs[max_in].getPage(x))
    else:
        for x in reversed(range(min_len, max_len)):  # todo fix so Index correct
            out_pdf.addPage(pdf_objs[max_in].getPage(x))

    with open(output_file, 'wb') as o_file:
        out_pdf.write(o_file)
