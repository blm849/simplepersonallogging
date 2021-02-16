#############################################################################
#
# easylog.py                                 
#
# Description:
#  
# This program logs into an XLSX file  
#
# History:
#
#       2020.02.16	Initial implementation. (BLM)
#
# Examples:
#
#       To call the program, enter: python easylog.py <inifile> 
#
#############################################################################

import ConfigParser				# needed to process the input file
import sys						# needed to process input parameters
from datetime import datetime   # need for date material
import openpyxl					# needed to extract data from Excel
import os						# To clear the screen


# Process the input parameters.
if len(sys.argv) == 1:
	iniFile = "easylog.ini"

elif len(sys.argv) == 2:
	iniFile = sys.argv[1]

else:
	print "going with the inifile of ", iniFile
# 	sys.exit()

"""
# The format of infile.ini is like this (minus the #). Note, no quote around the string
[DEFAULT]
xlsxFile = 2021log.xlsx
prompt1 = Bernie, enter what you want to record. Use these verbs and then a comment, seperated by a comma. Add another comma then verb for a subcategory
prompt2 = verbs: log (journaling) sleep mood weight happy(gratitude) kudos(wins) FF kids treats NEW fitness cooking reading writing IT art house $ politics diet food WORK org
"""

config = ConfigParser.ConfigParser()
config.read(iniFile)

xlsxFile = config.get('DEFAULT', 'xlsxFile')
prompt1 = config.get('DEFAULT', 'prompt1')
prompt2 =  config.get('DEFAULT', 'prompt2')

wb = openpyxl.load_workbook(xlsxFile)
ws = wb.active
# sheet = wb.get_sheet_by_name(inputSheet)

# Set new_name to something other than 'quit'.
the_input = '?'

# Start a loop that will run until the user enters 'quit'.
while the_input != '':
    if os.name == 'posix':
      os.system('clear')
    else:
      os.system('cls')
    
    # Ask the user for a name.
    print prompt1
    print prompt2
    the_input = raw_input()
    if the_input != '':
          try: 
             category, comment, subcategory = the_input.split(",") 
          except:
             category, comment = the_input.split(",") 
             subcategory = ""
	  #print the_year , the_week, the_day, the_date, the_time
	  now = datetime.now()
	  ws.append([now.strftime("%Y"), now.strftime("%W"), now.strftime("%a"), now.strftime("%x"),now.strftime("%X"), category, subcategory, comment])
	
wb.save(filename = xlsxFile)







