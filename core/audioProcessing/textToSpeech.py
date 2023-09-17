import os
import threading 
from gtts import gTTS 
from playsound import playsound

lock = threading.Lock()

#this function deals with converting text into speech
def  translate(text):
    with lock:
        path = os.getcwd()
        speach = gTTS(text)
        speach.save(path+'\\audioProcessing\\temp.mp3')
        playsound(path+'\\audioProcessing\\temp.mp3')
        os.remove(path+'\\audioProcessing\\temp.mp3')
    
#this function allows for multiple texts to be inputted while the TTS is currently running
#it is probably wise to avoid using this and instead work with translate for more control
def multithreadedTTS(text):
    print(text)
    thread = threading.Thread( target= translate, args=(text,) )  

    thread.start()
    


#for testing purposes
def terminal():

    while True:
        userInput = input("User: ")
        
        if userInput == 'exit':
            exit()
        else:
            translate(userInput)
        

if __name__ == '__main__':
    terminal()