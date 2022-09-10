import PyPDF2

#pdf_file = open('Check Your English Vocabulary for TOEFL.pdf', 'rb')
#pdf_file = open('101-Conversations.pdf', 'rb')
pdf_file = open('25scratch3gamesforkids_2.pdf', 'rb')

pdf_reader = PyPDF2.PdfFileReader(pdf_file)
pdf_writer = PyPDF2.PdfFileWriter()

for page_num in range(63, 67):
    page_num = pdf_reader.getPage(page_num)
    pdf_writer.addPage(page_num)

pdf_output_file = open('Colored_Walls.pdf', 'wb')

pdf_writer.write(pdf_output_file)

pdf_output_file.close()
pdf_file.close()
