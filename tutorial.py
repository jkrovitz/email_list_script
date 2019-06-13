# import sys
# from google.appengine.ext import vendor

# # Third-party libraries are stored in "lib", vendoring will make
# # sure that they are importable by the application.
# vendor.add('lib')

# def unload_module(module_name):
#     target_modules = [m for m in sys.modules if m.startswith(module_name)]
#     for m in target_modules:
#         if m in sys.modules:
#             del sys.modules[m]

# unload_module('oauth2client')
# unload_module('pyasn1_modules')

import gspread 

from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('creds.json', scope)

gc = gspread.authorize(credentials)

wks = gc.open('Test').sheet1

print(wks.get_all_records())