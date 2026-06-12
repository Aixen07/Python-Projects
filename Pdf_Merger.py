from pypdf import PdfMerger

merger = PdfMerger()

pdf_files = []
a = int(input("Enter how many pdfs you want to merge: "))

for i in range(0,a):
    name = input("Enter the Pdf Name: ")
    pdf_files.append(name)

for pdf in pdf_files:
    merger.append(pdf)

merger.write("merged_output.pdf")

merger.close()
