import os


wordbank = {}

def arrayToString(array):
    if array == None: 
        raise KeyError
    string = ""
    for i in array:
        string = string + i 
        string = string + " "
        
    return string[:len(string)-1]
        

#this is an attempt to make a counting function for the number of each phrase that comes up following a word in a sentence
def recursiveFunction(sentence, i,  bank = wordbank):
    Punctuation = {'.','?','!' }
    
    if sentence == None: return             # no word was entered
    if sentence[0] == None: return          # no word was entered
    if len(sentence) < i: return           # making sure i is smaller than len(sentence)
    if sentence[0] in Punctuation : return          #punctuation that ends the sentence



    
    firstWord= sentence[0]
    phrase = arrayToString(sentence[1:i])

    
    if firstWord not in wordbank:           #checking if first word is in the wordbank
        wordbank[firstWord] = {".":1}       #adding word to dictionary
        
    

    
    
    if (phrase not in wordbank[firstWord]):     #checking if the phrase is already recorded for that word

        if phrase != "" :
            wordbank[firstWord][phrase] = 1         # if not it adds it to possible outcomes    
    
    else: wordbank[firstWord][phrase] = wordbank[firstWord][phrase]+1        #otherwise it will increase its probability of showing
    
    if len(sentence) == i: return wordbank
     
    recursiveFunction(sentence, i+1) #recursing here
    

def nonRecursiveFunction(sentence, wordbank=wordbank):
    for i in range(len(sentence)):
        recursiveFunction(sentence[i:],0 ,bank=wordbank)
    

def start(wordbank = wordbank):


    path = os.getcwd()+"\\AI"
    with open(path+"\\cleanedDataset2.txt",'r', encoding="iso-8859-1") as dataset:
        for i in range(0,577738):
            print(i,"/556265")
            line = dataset.readline().strip()
            sentence = line.split()
            nonRecursiveFunction(sentence, wordbank)
    
    with open(path+"\\wordbank.txt",'w', encoding="iso-8859-1") as file:
        file.write(str(wordbank))
        
    NumWordTranslation = {}

    Data = wordbank
    for startingWord in Data.keys():
        count = 0 
        NumWordTranslation[startingWord] = {}
        
        for phrase in Data[startingWord].keys():
            NumWordTranslation[startingWord][count] = phrase 
            count += Data[startingWord][phrase]
            

    with open(path+"\\NumWordTranslation.txt",'w') as output:
        output.write(str(NumWordTranslation))
            


#for testing purposes
def terminal():

    while True:
        userInput = input("User: ")
        print(userInput)
        
        if userInput == 'exit':
            exit()
        elif userInput == 'start':
            start()
        else:
            userInput = userInput.split()
            nonRecursiveFunction(userInput, 0)
            print(wordbank)
            
        

if __name__ == '__main__':
    terminal()













