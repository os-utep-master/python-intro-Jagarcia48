#Jorge Garcia
#CS4310
#August 28,2019
#citations: https://www.w3schools.com/python/python_file_write.asp, stackoverflow.com, Erik Macik
#Update: finished sorting working on reading file and writting

import sys
import re
import os

fileNameInput = sys.argv[1]
fileNameOutput = sys.argv[2]

dictionaryWords = {}

#Erick Macik helped me with the dictionary storage from line 23 to 28. My original code lacked the usage of a dictionary.
with open(fileNameInput, 'r') as inputFile:
    for line in inputFile:
        words = line.split()
        for word in words:
            #Used to remove the punctuations
            word = word.strip(".,!?:;'\"") 
            word = word.lower()
            if word == '':
                continue
            if word in dictionaryWords:
                dictionaryWords[word] += 1
            else:
                dictionaryWords[word] = 1

outputFile = open(fileNameOutput, 'w')
for key in sorted(dictionaryWords):
    outputFile.write(key + " " + str(dictionaryWords[key]) + "\n")