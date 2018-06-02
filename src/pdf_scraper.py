import PyPDF2

file_object = open('data/NRPP.pdf', 'rb')

# creating a pdf reader object
pdf_reader = PyPDF2.PdfFileReader(file_object)

# printing number of pages in pdf file
print(pdf_reader.numPages)

# creating a page object
nepali_list = []
for i in range(25, 30):
    page_object = pdf_reader.getPage(i)
    nepali_list.append(page_object.extractText())


# print(nepali_list)

the_file = open('data/shabda.txt', 'w')


for item in nepali_list:
    the_file.write("%s\n" % item)

file_object.close()
