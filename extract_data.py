import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('INSERT_google_api_credential_file.json', scope)
client = gspread.authorize(creds)


worksheet_list_raw = client.open('INSERT_google_sheet_file_name').worksheets()
extracted_data = dict()


for w_sheets in worksheet_list_raw:
    sheet = client.open('INSERT_google_sheet_file_name').worksheet(w_sheets.title)
    extracted_data[w_sheets.title] = sheet.get_all_values()

