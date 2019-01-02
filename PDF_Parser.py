import PyPDF2

sample_file_1 = 'Sample_PDF_2.pdf'

pdf_file_object = open(sample_file_1, 'rb')

pdfReader = PyPDF2.PdfFileReader(pdf_file_object)

num_of_pages = pdfReader.numPages
count = 0 
text = ''

while count < num_of_pages:
    page_object = pdfReader.getPage(count)
    count += 1 
    text += page_object.extractText()

print(text)

if text != '':
    text = text