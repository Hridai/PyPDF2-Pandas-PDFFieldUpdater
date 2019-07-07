# Filling In PDF Fields With Data Found In a .csv & Saving Copies using PyPDF2 and Pandas

This is a simple guide to populating a .pdf with editable fields programatically - with data found in a .csv file and saving a copy of this pdf for every row found in the dataset.

## Requirements
Libraries: PyPDF2, Pandas
```python
pip install PyPDF2
pip install Pandas
```

## Directories, Files explained
```
- Root
  - In        Contains the .pdf file with the editable fields and the .csv containing the input data
  - Out       Will contain the output .pdf with the fields filled in
  - Images    Screenshots/images used for this page
```

## Adapting The Code To Your Requirements
All the code lives in **pdfProcessor.py**
The only variables that need amending are:
```
  - csvin     the path to the .csv file
  - infile    the pdf form you are trying to affect
  - outfile   the directory where the final versions will be output
  - field_dictionary    Key Value pairs. Keys are the field names in the pdf you are trying to change, the values what you want to write into them
```
You will need the **exact** field names for each field you are trying to change in the pdf. Note this will not necessarily be the label next to the textbox you are writing to, but will be the name assigned to the textbox itself. This is how to get that value:

```python
from PyPDF2 import PdfFileReader
infile = "C:\\Your File Path\\YourPDF.pdf"
pdf = PdfFileReader(open(infile, "rb"), strict=False)
fields = pdf.getFields()
```
The dictionary is now output to the _fields_ variable. There is a good chance this is not viewable in your locals due to it's large size. Type this variable name into the console to see the output if this is the case- and decipher the field names. The field names in the example file that comes with this directory (PatientIntakeForm.pdf) will output the below. The field names visible in the below snippet are __Address[0]__ and __Age[0]__ and __CellNum[0]__
These are what will need to be passed as keys into the variable _field_dictionary_ to write to these fields.

```python
fields
Out[5]: 
{'Address[0]': {'/FT': '/Tx',
  '/Ff': 8388608,
  '/Parent': {'/Kids': [IndirectObject(194, 0),
    IndirectObject(195, 0),
    IndirectObject(196, 0),
    IndirectObject(197, 0),
    IndirectObject(198, 0),
    IndirectObject(199, 0),
    IndirectObject(200, 0),
    IndirectObject(201, 0),
    IndirectObject(22, 0),
    IndirectObject(203, 0),
    IndirectObject(204, 0),
    IndirectObject(205, 0),
    IndirectObject(206, 0),
    IndirectObject(207, 0),
    IndirectObject(208, 0),
    IndirectObject(209, 0)],
   '/Parent': {'/Kids': [IndirectObject(19, 0),
     IndirectObject(20, 0),
     IndirectObject(183, 0),
     IndirectObject(184, 0),
     IndirectObject(185, 0),
     IndirectObject(186, 0),
     IndirectObject(187, 0),
     IndirectObject(188, 0),
     IndirectObject(189, 0),
     IndirectObject(190, 0),
     IndirectObject(191, 0),
     IndirectObject(192, 0),
     IndirectObject(193, 0),
     IndirectObject(21, 0),
     IndirectObject(210, 0),
     IndirectObject(211, 0),
     IndirectObject(212, 0),
     IndirectObject(213, 0),
     IndirectObject(214, 0)],
    '/Parent': {'/Kids': [IndirectObject(18, 0)], '/T': 'form1[0]'},
    '/T': 'Page1[0]'},
   '/T': 'PatientInformation[0]'},
  '/T': 'Address[0]',
  '/TU': 'Address'},
 'Age[0]': {'/FT': '/Tx',
  '/Ff': 8388608,
  '/Parent': {'/Kids': [IndirectObject(194, 0),
    IndirectObject(195, 0),
    IndirectObject(196, 0),
    IndirectObject(197, 0),
    IndirectObject(198, 0),
    IndirectObject(199, 0),
    IndirectObject(200, 0),
    IndirectObject(201, 0),
    IndirectObject(22, 0),
    IndirectObject(203, 0),
    IndirectObject(204, 0),
    IndirectObject(205, 0),
    IndirectObject(206, 0),
    IndirectObject(207, 0),
    IndirectObject(208, 0),
    IndirectObject(209, 0)],
   '/Parent': {'/Kids': [IndirectObject(19, 0),
     IndirectObject(20, 0),
     IndirectObject(183, 0),
     IndirectObject(184, 0),
     IndirectObject(185, 0),
     IndirectObject(186, 0),
     IndirectObject(187, 0),
     IndirectObject(188, 0),
     IndirectObject(189, 0),
     IndirectObject(190, 0),
     IndirectObject(191, 0),
     IndirectObject(192, 0),
     IndirectObject(193, 0),
     IndirectObject(21, 0),
     IndirectObject(210, 0),
     IndirectObject(211, 0),
     IndirectObject(212, 0),
     IndirectObject(213, 0),
     IndirectObject(214, 0)],
    '/Parent': {'/Kids': [IndirectObject(18, 0)], '/T': 'form1[0]'},
    '/T': 'Page1[0]'},
   '/T': 'PatientInformation[0]'},
  '/T': 'Age[0]',
  '/TU': 'Age'},
 'CellNum[0]': {'/FT': '/Tx',
  '/Parent': {'/Kids': [IndirectObject(194, 0),
    IndirectObject(195, 0),
    IndirectObject(196, 0),
```

## Support or Contact
Run into any bugs or have further questions? Drop me an e-mail HridaiTrivedy@gmail.com
