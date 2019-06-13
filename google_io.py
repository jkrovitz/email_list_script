import gspread
import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

json_key = json.load(open('creds.json')) # json credentials you downloaded earlier
scope = ['https://spreadsheets.google.com/feeds']

credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'].encode(), scope) # get email and key from creds

file = gspread.authorize(credentials) # authenticate with Google
sheet = file.open("MUO_Python_Sheet").sheet1 # open sheet