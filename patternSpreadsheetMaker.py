# imports
import os
import json
from openpyxl import Workbook

from uniqueReadableData import makeReadableString, makeRandomInt, makeRandomReal

# Parameters
#where to find pattern(s) JSON
#pattern_loc = r"C:\Users\aschultheis3\Box\General\_Repos\LIPFork-rapid-modeling-tools\ingrid\src\model_processing\patterns"
#pattern_loc = r"C:\Users\aschultheis3\Box\General\MSFTB\Pattern Development\New Patterns"
pattern_loc = r"C:\Users\aschultheis3\Box\General\RMT Testing\Pattern Tests\TEMP patterns to read in"


#where to put the output files (set as "" to use pattern_loc)
#output_loc = r"C:\Users\aschultheis3\Box\General\RMT Testing\Pattern Tests"
output_loc = r"C:\Users\aschultheis3\Box\General\RMT Testing\Pattern Tests\mostly working test set A"

rows = 10 #number of rows to randomly populate for pattern(s)

# Defs 

def makePatternTestSpreadsheet(name,pattern,n_rows):
	'''
	makes a spreadsheet based on the content of a RMT pattern JSON file. For each column identified in the pattern
	'''
	wb = Workbook()
	ws = wb.active
	# name worksheet based on pattern name (to work with Ingrid)
	ws.title = name

	header = []
	# go through json file's "Columns to Navigation Map" for spreadsheet header info
	for key in pattern['Columns to Navigation Map']:
		header.append(key)
	ws.append(header)

	# populate random values
	for i in range(rows):
		row = []
		for j in header:
			row.append(makeReadableString())
		ws.append(row)


	# save spreadsheet (name workbook based on pattern name)
	wb.save(output_loc + '\\' + name + '.xlsx')
	return


def populateOtherData():
	# TODO: make a function that can be run in additon to makePatternTestSpreadsheet() that looks at an optional additional file specifying specific types of data to write for columns,
	# specifically handling random non-string values (random strings are already handled)


	#
	#


	if dataType == 'Integer':
		# TODO: random Integer in specified range

		# use uniqueReadableData.makeRandomInt()

		a = 1

	elif dataType == 'Real':
		# TODO: random Real in specified precision
		# excel might to weird things to this, tbd

		# use uniqueReadableData.makeRandomReal()

		a = 1

	elif dataType == 'Complex':
		# TODO (eventually): random Complex Number
		# these will be for however MagicDraw/Cameo expects booleans to be populated, need to figure that out

		# use uniqueReadableData.makeRandomReal() to populate each part of the complex number

		a = 1

	elif dataType == 'Boolean':
		# TODO (eventually): random Boolean
		# these will be for however MagicDraw/Cameo expects booleans to be populated, need to figure that out

		# just do this one here since it will likely just be choosing from two strings

		a = 1
	#
	#

	return


def populateFromEnumeration():
	# TODO: make a function that can be run in additon to makePatternTestSpreadsheet() that looks at an optional additional file specifying specific types of data to write for columns,
	# specifically handling enumerations from a predefined set

	# for the column in question, choose randomly from the enumeration values specified 


	return

if output_loc == "":
	output_loc = pattern_loc


# get all of the json files in a directory (assuming they are all valid RMT pattern files) and make a test spreadsheet for each one

patterns = {}
for fn in os.listdir(pattern_loc):
	if fn.endswith(".json"):
		#print(fn.split(".json")[0])
		name = fn.split(".json")[0]
		print("opening file: " + fn)
		with open(pattern_loc + '\\' + fn) as f:
			patterns[name] = json.load(f)
		print("data pulled from: " + fn)

for key in patterns:
	makePatternTestSpreadsheet(key,patterns[key],rows)
	print("spreadsheet generated for " + key + " pattern")


