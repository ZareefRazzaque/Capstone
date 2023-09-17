import requests
import os

def get_text_from_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors

        # Assuming the website is using UTF-8 encoding. Adjust if necessary.
        text_data = response.text

        return text_data
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)
        return None

if __name__ == "__main__":
    path = os.getcwd()+"\\AI"
    
    with open(path+"\\cleanedDataset.txt", "w", encoding="utf-8") as file:
        while True:
            url = input("URL:")  

            text_data = get_text_from_url(url)

            if text_data:
                
                text_data = text_data.lower()
                text_data = text_data.replace("\n","")
                
                text_data = text_data.split(" ")
                
                
                asterixNum = 0
                sentence= ""
                
                for i in text_data:
                    
                    if  ("*" in i): 
                        asterixNum += 1
                        
                        
                    if asterixNum == 2:
                        sentence = sentence + i + " "
                        try:    
                                if i[-1] in {".","?","!",":"}:
                                    sentence += "\n"
                                    file.writelines(sentence)
                                    sentence= ""
                        except: pass
                
                
                print("Text data saved to output.txt")
                
                
                


