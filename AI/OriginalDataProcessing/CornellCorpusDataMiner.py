import os
import re

path = os.getcwd()+"\\AI\\OriginalDataProcessing"
with open(path+"\\linesOnly.txt", "r", encoding="iso-8859-1") as dataset:
    with open(path+"\\cleanedDataset2.txt",'w', encoding="utf-8") as file:
        data = dataset.read().lower()
        parts = data.replace("!", " !\n")
        parts = parts.replace("?", " ?\n")
        parts = parts.replace(".", " .\n")
        parts = parts.replace(".\n .\n .", " ...")
        parts = parts.replace(", ", " , ") 
        parts = parts.replace("\n ", "\n")
        parts = parts.replace("\n\n", "\n")
        parts = parts.replace("\n ...\n", "\n")
        parts = parts.replace("[","")
        parts = parts.replace("]","")
        parts = parts.replace("{","")
        parts = parts.replace("}","")
        parts = parts.replace("\"","")
        
        parts = re.sub(r"<.*?>", "", parts)  # Removes HTML tags
        parts = parts.strip()
        
        check = parts

        while True:
            if check == parts:
                break
            else: 
                parts.replace('\n\n',"\n")
        
        
        

        file.writelines(parts)
        print(parts)

            
            
