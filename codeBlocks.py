#To get list of the tab sheets in the Google Sheets Workbook
worksheet_list = workbook.worksheets()
print(worksheet_list)
#To get just the titles of each tab sheets
sheets = map(lambda x: x.title, workbook.worksheets())
print(list(sheets))



#To Retrieve a value of a cell
value = C1.cell(7,8).value
print(value)
value1 = C1.acell("H7").value
print(value1)
value2 = C1.acell('H7').value
print(value2)



#To perform simple calculation on a column 
C1.update_cell(8, 5, "=sum(E2:E7)")
#To use a formula 
C1.update([['=SUM(F2:F7)']], 'F8', raw=False)

#To perform calculations on rows
#This works BUT what if we want to update all the rows under it using the Google sheets formula, it seems fixed when wanting to compare to the next row under F2 
for i in range(2,8):
    C2.update_cell(i, 9, '=IF(F2 = 0, "Cleared", "Balance Due")')
#So, here I created the code in python to do just that!
for i in range(2, 8):
    if C2.cell(i, 6).value == str(0):
        C2.update_cell(i, 9, "Cleared")
    else:
        C2.update_cell(i, 9, "Balance Due")



#To get the values of a row
GN = workbook.worksheet("GN") # A variable to refer to the Google sheets tab named "GN"
row_values_list_of_GN = GN.row_values(2) #row_values in second row
print("Rows Values of row 2 in sheet GN:")
print(row_values_list_of_GN)



#To get a range of values (list of lists) and updating a range of cells with it
res = C1.get('A1:B7')
pprint(res)

C1.update('I1:J7', res)



#To delete a row or range of rows 
GN.delete_rows(3,5) #deletes rows 3 to 5 inclusive



#To clear the values of a range of cells (within a column)
for i in range(2,5):
    GN.update_acell('H' + str(i), '')

#To clear the values of a range of cells (within a row)
#First we import a string called ascii_uppercase, this conatins the alphabet letters String 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from string import ascii_uppercase
#We substring the string to choose only the letter that we want. Its index starts at 0(A)-25(Z)
letters = ascii_uppercase[2:5] #This creates a substring of alphabet letter String 'CDE' [index start inclusive:index end exclusive]
for element in range(0, len(letters)):
    GN.update_acell(letters[element] + str(4), '')

# NOTE: This could be easier if you just use update_cell(#,#,SomeValue)



#To copy a range of cells to another sheet tab
cellscopy = C1.get("A2:H7") # getting the values of the cells in this range
pprint(cellscopy)

GN = workbook.worksheet("GN") # A variable to refer to the Google sheets tab named "GN"
GN.update("A2:H7", cellscopy) #update the values in the cell range in tab GN



# If cells Name Match, Copy over notes within workbook tabs
for i in range(2, 8):
    for j in range(2, 5):
        if C1.cell(i, 1).value == GN.cell(j, 1).value:
            GN.update_cell(j, 8, C1.cell(i, 8).value)
            # print("Cell C1 " + C1.cell(i,1).value + " Matches cell GN " + GN.cell(j,1).value)        
            # print(C1.cell(i, 8).value)
#if you prefer to use acell to know the cell By Letter+Number
for i in range(2, 8):
    for j in range(2, 5):
        if C1.acell("A" + str(i)).value == GN.acell("A" + str(j)).value:
            GN.update_acell("H" + str(j) , C1.acell("H" + str(i)).value)



#Copy over to another Google sheet. Note: Make sure to Share Google Sheets by going to Google Cloud Console> APIs&Services> credentials> copy Email>  paste on the Google Sheets Share button 
sheet_id2 = "1O0bJfFMztvQX3sW_sXC0yGUk88zTA6xn7SpIw88ZXto"
workbook2 = client.open_by_key(sheet_id2)
print(workbook2.title)

C33 = workbook2.worksheet("C33")

copyTOwk2 = C3.get("A1:H7")
C33.update("A1:H7", copyTOwk2)

C33.update_acell("A1", "Name C33")



#Copy over to another Google Sheets workbook if the Name column matches(if its there)
for i in range(2, 8):
    for j in range(2, 5):
        if C3.cell(i, 1).value == C33.cell(j, 1).value:
            C33.update_cell(j, 8, C3.cell(i, 8).value)



#To find a Clients Name in Google sheet tab C1
pdfNameTitle = "Marco"  #We will extract the pdfFile Name part
cell = C1.find(pdfNameTitle) #We will search for it in C1 GoogleSeet tab

try:
    if cell.value == pdfNameTitle:  #if found do this
        print("Client Name found on: ")
        print(cell.row, cell.col)
        print(cell.value)
except AttributeError:      #if not found do this
    print("Not Found")



#To find Clients Name value in C1, retrieve their Email Address, update cell and color its text
pdfNameTitle = "Marco"  #We will extract the pdfFile Name part
cell = C1.find(pdfNameTitle) #We will search for it in C1 GoogleSeet tab

try:
    if cell.value == pdfNameTitle:  #if found do this
        print("Client Name found on: ")
        print(cell.row, cell.col) #row, column
        print(cell.value) #value is the Client Name
        print("Client Named " + cell.value + " email address is:")
        print( C1.cell(cell.row, 4).value ) #Retrieve their Email Address
        #Write into Google Sheets update cell with text in light blue color for receipt sent
        C1.update_cell( cell.row, 8, "AV - Receipt sent" ) #update cell text
        C1.format( "H" + str(cell.row), {"textFormat": {"foregroundColor": {"red": 184, "green": 53, "blue": 53}}} ) #color text in light blue
except AttributeError:      #if not found do this
    print("Not Found")



#To find the Name value in each Google sheets tab

#To get the titles of each tab sheets, the problem with this is cell.value object has no attribute value.
"""
sheets = map(lambda x: x.title, workbook.worksheets())
pdfNameTitle = "Bob" 
for Sheetname in sheets:
    cell = Sheetname.find(pdfNameTitle)
    try:
        if cell.value == pdfNameTitle: 
            print("Client Name found on:")
            print(cell.row, cell.col)
            print(cell.value)
            print("Found in Sheet: " + Sheetname)
    except AttributeError:
        print("Not Found")
"""



#Extract Name part of the pdf File
fileName = "Client Name - Balance Sheet"
print(fileName)
ClientName = fileName.split("-")[0]
print(fileName.split("-")[0])
print(ClientName)



#To extract the Name part of the pdf File and find it in Google Sheets
pdfFile = "Bob - Balance Sheet"  #We will extract the pdfFile Name part
ClientName = pdfFile.split(" ")[0] #Put that name into a variable
cell = C1.find(ClientName) # Will find that name in Google sheets C1 tab
print(cell.value) #Have name printed it out
print(cell.row, cell.col) #print out the row and column of where it was found





#All together for a Google Sheets Tab, Exctracts Name, Finds Name, Finds Email, Updates Cell to Receipt Sent, and changes text color
pdfFile = "Bob - Balance Sheet"  #We will extract the pdfFile Name part
ClientName = pdfFile.split(" ")[0] #Put that name into a variable

cell = C1.find(ClientName) # Will find that name in Google sheets C1 tab

print("Client Name found on row " + str(cell.row) + " column " + str(cell.col)) #row, column of where it was found in Google Sheets

print("Client name is: " + cell.value) #Have name printed out

print("Client Named " + cell.value + " email address is:")
print( C1.cell(cell.row, 4).value ) #Retrieve their Email Address

#Write into Google Sheets update cell with text in light blue color for receipt sent
C1.update_cell( cell.row, 8, "AV - Receipt sent" ) #update cell text
C1.format( "H" + str(cell.row), {"textFormat": {"foregroundColor": {"red": 184, "green": 53, "blue": 53}}} ) #color text in light blue

