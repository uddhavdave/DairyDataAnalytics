import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds= ServiceAccountCredentials.from_json_keyfile_name('dairtymanager-d5500dfa8dc2.json',scope)
client=gspread.authorize(creds)

sheet = client.open('Cow Sasan - lot 1 & 2 & 3').get_worksheet(0)
sheet1 = client.open('COW milk').get_worksheet(1)
pp = pprint.PrettyPrinter()



result = sheet.col_values(2)
pp.pprint(result)