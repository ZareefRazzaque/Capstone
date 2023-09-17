import os


path = os.getcwd()+"\\AI"

with open(path+"\\dataset.txt", encoding="utf-8") as dataset:
    with open(path+"\\cleanedDataset.txt",'w', encoding="utf-8") as cleanedData:
        
        data = dataset.read().lower()
        data = data.split(" ")

        sentence= ""
        for i in data:
            sentence = sentence + i + " "
            if i[-1] in {".","?","!",":"}:
                sentence += "\n"
                cleanedData.writelines(sentence)
                sentence= ""
                
            
                
            
        
        
        
        