import PyPDF2

def open_Pdf(pdf):
	pdf_file = open(pdf, 'rb')
	arch_pdf = PyPDF2.PdfFileReader(pdf_file)
	return arch_pdf

def get_Text(arch_pdf, pg_number):
	page = arch_pdf.getPage(pg_number)
	text = page.extractText()
	return text

pdf = input('PDF_link>>> ')
page = int(input('Pagina>>> '))

arch_pdf = open_Pdf(pdf)
text = get_Text(arch_pdf, page)

print(text)

