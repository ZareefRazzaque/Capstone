import os


path = os.getcwd()+"\\AI"
with open(path+"\\wordbank.txt",'r') as dataset:
    Data = eval(dataset.read())

    NumWordTranslation = {}

    for startingWord in Data.keys():
        count = 0 
        NumWordTranslation[startingWord] = {}
        
        for phrase in Data[startingWord].keys():
            NumWordTranslation[startingWord][count] = phrase 
            count += Data[startingWord][phrase]
            

    with open(path+"\\NumWordTranslation.txt",'w') as output:
        output.write(str(NumWordTranslation))
            
    print(NumWordTranslation)