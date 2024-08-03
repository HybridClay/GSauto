import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1HZZtuGkm5k7GDo78E-vI4VlB6FAEPexoURnPHEqvaYQ" #the SheetID can be found in the URL after the d/ to refer to the Google Sheets we want to work in
workbook = client.open_by_key(sheet_id) #a variable to refer to that Google Sheet workbook
#print(workbook.title)


C1 = workbook.worksheet("C1") # A variable to refer to the Google sheets tab named "C1"

GN = workbook.worksheet("GN") 

C2 = workbook.worksheet("C2")

C3 = workbook.worksheet("C3")



sheet_id2 = "1O0bJfFMztvQX3sW_sXC0yGUk88zTA6xn7SpIw88ZXto"  #The SheetID for another workbook found in its URL after the d/....
workbook2 = client.open_by_key(sheet_id2) #a variable to refer to that Google Sheet workbook
# print(workbook2.title)  #print the title of that google sheets workbook

C33 = workbook2.worksheet("C33") # A variable to refer to that Google sheets tab named "C33"




#Copy&Paste a code block from codeBlocks.py HERE:

