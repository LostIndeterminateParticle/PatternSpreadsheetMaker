# imports
import json
import random

# data sources
words_loc = 'words.json'

# parameters:
# strings
n_combo = 3 # number of words to string together for Readable Strings
string_sep = '' #I think it is best to keep this blank unless it is known that all possible uses will accept whatever character is used as the separator
# Integers

# Reals

# Complex Numbers



def makeReadableString():
	with open(words_loc, 'r') as f:
		words = json.load(f)

	n = len(words)
	for i in range(n_combo):
		word_num = random.randint(0,n-1)
		if i > 0:
			readableName = readableName + string_sep + words[word_num].capitalize()
		else:
			readableName = words[word_num].capitalize()

	return readableName


def makeRandomInt():
	# TODO
	return

def makeRandomReal():
	# TODO

	return