# PatternSpreadsheetMaker

A simple utility for Rapid Modeling Tools which will read in the pattern files in a directory and populate an appropriately-formatted .xlsx file with the required column headers and row(s) of random words.
These .xlsx files can then be used with Ingrid to produce input files for Player Piano, enabling some end-to-end testing (and debugging) of Rapid Modeling Tools with a given pattern.

To run:
In [patternSpreadsheetMaker.py](patternSpreadsheetMaker.py) specify the location of patterns to read, the location to put the output .xlsx files, and how many rows to populate with random words. Then run [patternSpreadsheetMaker.py](patternSpreadsheetMaker.py)

## TODO

### stuff to add to the player piano data generator

should add an option to go in and select one or more columns to populate with (vs the default words):
* random integers
* random floats
* random selection from numbers (as if from an enumeration)
* specific strings (as if from an enumeration)

maybe I could have it default to doing the words in all the cells, then look for an optional additional related file that contains details the type of info to fill in for any columns called out in that file and go through and replace the initial cells


The content of words.json pulled from [mnemonic-words](https://github.com/sindresorhus/mnemonic-words), with license: MIT © [Sindre Sorhus](https://sindresorhus.com)