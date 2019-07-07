from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject
import pandas as pd

def set_need_appearances_writer(writer: PdfFileWriter):
    try:
        catalog = writer._root_object
        if "/AcroForm" not in catalog:
            writer._root_object.update({
                NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})
        need_appearances = NameObject("/NeedAppearances")
        writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
        return writer

    except Exception as e:
        print('set_need_appearances_writer() catch : ', repr(e))
        return writer

csvin = "H:\\gitprojects\\\PyPDF2-Pandas-PDFFieldUpdater\\in\\data.csv"
infile = "H:\\gitprojects\\\PyPDF2-Pandas-PDFFieldUpdater\\in\\PatientIntakeForm.pdf"
data = pd.read_csv( csvin )
pdf = PdfFileReader(open(infile, "rb"), strict=False)  
if "/AcroForm" in pdf.trailer["/Root"]:
    pdf.trailer["/Root"]["/AcroForm"].update(
        {NameObject("/NeedAppearances"): BooleanObject(True)})
fields = pdf.getFields() # Run in console to see Key names for field entry

i = 0 #Filename numerical prefix
for j, rows in data.iterrows():
    outfile = "H:\\gitprojects\\\PyPDF2-Pandas-PDFFieldUpdater\\out\\"
    i += 1
    
    pdf2 = PdfFileWriter()
    set_need_appearances_writer(pdf2)
    if "/AcroForm" in pdf2._root_object:
        pdf2._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    
    if "/AcroForm" in pdf2._root_object:
        pdf2._root_object["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
        
    field_dictionary = {"PatientFirstNameMain[0]": rows['FirstName'], "PatientLastNameMain[0]": rows['LastName'], 
                        "Age[0]": rows['Age'], "CellNum[0]" : rows['Cellnum']}
    
    outfile = outfile + str(i) + '_out.pdf'
    pdf2.addPage(pdf.getPage(0))
    pdf2.updatePageFormFieldValues(pdf2.getPage(0), field_dictionary)
    outputStream = open(outfile, "wb")
    pdf2.write(outputStream)