import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets"]
creds = ServiceAccountCredentials.from_json_keyfile_name("service_account.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Portfolio Tracker")
worksheet = spreadsheet.sheet1

worksheet.update('A1', 'Hello, Google Sheets!') 
worksheet.append_row(['New', 'Row', 'Data'])  

print("Data written to Google Sheet.")