#Jorge Garcia
#CS4310
#August 28,2019
#Update: finished sorting working on reading file and writting
print("Name the output file:")
fileName = input()
def wordCount(input):
    myfile = open(input)
    lines = myfile.readlines()

    # creates empty lists to store words and keep track of # of words used
    wordlist = []
    counter = []

    for line in lines:
        # get all the words in the current line
        words = line.split()
        # iterates through each individual word 
        for word in words:
            # removes punctuations
            # makes the words case insensitive
            word = word.strip(".,!?:;'\"") 
            word = word.lower()

            if word not in wordlist:
                wordlist.append(word)

            # adds new word to counter
            counter.append(word)

    wordlist.sort()
    f = open(fileName, "w+")
    for word in wordlist:
        print(word, counter.count(word))
        f.write(word +" "+ str(counter.count(word)) + "\n")
        

print("What file do you want to organize?")

wordCount(input())







#words = sorted(open("declaration.txt").read().split(),key = str.casefold)
#print(words)



#f = open("declaration.txt", "r")

#words = sorted(f.read().split(), key = str.casefold)

#for  in words:
#    print(word)


#words = sorted(open("declaration.txt").read().split())
#print(words)
#
#f = open("speech.txt", "r")
#print(f.read())
#

