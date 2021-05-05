import pandas as pd
import os
from PyPDF2 import PdfFileWriter, PdfFileReader
from PyPDF2.generic import BooleanObject, NameObject, IndirectObject


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

if __name__ == '__main__':
    csv_filename = "EISAutoFill.csv"
    pdf_filename = "EIS 3 Certificate - Autofilled.pdf"
    
    csvin = os.path.normpath(os.path.join(os.getcwd(),'in',csv_filename))
    pdfin = os.path.normpath(os.path.join(os.getcwd(),'in',pdf_filename))
    pdfout = os.path.normpath(os.path.join(os.getcwd(),'out'))
    data = pd.read_csv(csvin)
    pdf = PdfFileReader(open(pdfin, "rb"), strict=False)  
    if "/AcroForm" in pdf.trailer["/Root"]:
        pdf.trailer["/Root"]["/AcroForm"].update(
            {NameObject("/NeedAppearances"): BooleanObject(True)})
    pdf_fields = [str(x) for x in pdf.getFields().keys()] # List of all pdf field names
    csv_fields = data.columns.tolist()
    
    i = 0 #Filename numerical prefix
    for j, rows in data.iterrows():
        i += 1
        pdf2 = PdfFileWriter()
        set_need_appearances_writer(pdf2)
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        
        if "/AcroForm" in pdf2._root_object:
            pdf2._root_object["/AcroForm"].update(
                {NameObject("/NeedAppearances"): BooleanObject(True)})
        
        # Key = pdf_field_name : Value = csv_field_value
        field_dictionary_1 = {"Full Name": str(rows['FullName']),
                            "Address Line 1": rows['AddressLine1'],
                            "Address Line 2": rows['AddressLine2'],
                            "Address Line 3": rows['AddressLine3'],
                            "Post Code": rows['PostCode'],
                            "Description of Shares": rows['DescriptionOfShares'],
                            "Nominal Value of each Share": rows['NominalValueOfEachShare'],
                            "Number of Shares Issued": rows['NumberOfSharesIssued'],
                            "Amount Subscribed": rows['AmountSubscribed'],
                            "Share Issue Date": rows['ShareIssueDate'],
                            "Termination Date of these Shares": rows['TerminationDateOfTheseShares'],
                            "Received any value?": rows['ReceivedAnyValue?'],
                            "Name of Company Representative": rows['NameOfCompanyRepresentative'],
                            "Company Name": rows['CompanyName'],
                            "Unique Investment Reference Number": rows['UniqueInvestmentReferenceNumber'],
                            "Capacity in which signed": rows['CapacityInWhichSigned'],
                            "Registered Office Address Line 1": rows['RegisteredOfficeAddressLine1'],
                            "Registered Office Address Line 2": rows['RegisteredOfficeAddressLine2'],
                            "Registered Office Address Line 3": rows['RegisteredOfficeAddressLine3'],
                            "Date Signed": rows['DateSigned'],
                            "Post Code 2": rows['RegisteredOfficePostCode'],
                            }

        temp_out_dir = os.path.normpath(os.path.join(pdfout,str(i) + 'out.pdf'))
        pdf2.addPage(pdf.getPage(0))
        pdf2.updatePageFormFieldValues(pdf2.getPage(0), field_dictionary_1)
        pdf2.addPage(pdf.getPage(1))
        pdf2.addPage(pdf.getPage(2))
        pdf2.addPage(pdf.getPage(3))
        outputStream = open(temp_out_dir, "wb")
        pdf2.write(outputStream)
        outputStream.close()
    print(f'Process Complete: {i} PDFs Processed!')