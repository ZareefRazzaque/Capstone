from pygame import mixer
import os
import threading
from gtts import gTTS 

lock = threading.Lock()

#this function deals with converting text into speech along with sending it off to alexa
def  translateAndSend(text):
    try:mixer.init(devicename='CABLE Input (VB-Audio Virtual Cable)')       #virtual cable allows audio to be heard by alexa app
    except: pass
    
    with lock:                                                          
        path = os.getcwd()
        speach = gTTS(text)                                                 # we are using google's tts here (does the job for now) #TODO
        speach.save(path+'\\core\\audioProcessing\\temp.mp3')               #saving file so it can be read
        
        mixer.music.load(path+'\\core\\audioProcessing\\temp.mp3')          #loading and playing audio here
        mixer.music.play()
    
        while mixer.music.get_busy(): pass                                  #closing the mixer so that the audio file may be deleted
        mixer.music.stop()
        mixer.quit()
        os.remove(path + '\\core\\audioProcessing\\temp.mp3')               
        

#converts text to tts audio file (for testing purposes)
def translate(text):
    try:mixer.init()       
    except: pass
    path = os.getcwd()
    
    audio = gTTS(text)   
    audio.save(path+'\\core\\audioProcessing\\audio.mp3')
        
    mixer.music.load(path+'\\core\\audioProcessing\\audio.mp3')
    mixer.music.play()
    
    while mixer.music.get_busy():pass
    mixer.music.stop()
    mixer.quit()
    
    
    
    
#this function allows for multiple texts to be inputted while the TTS is currently running
#it is probably wise to avoid using this and instead work with translate for more control
def multithreadedTTS(text):
    print(text)
    thread = threading.Thread( target= translateAndSend, args=(text,) )  

    thread.start()



#for testing purposes
def terminal():

    while True:
        userInput = input("User: ")
        
        if userInput == 'exit':
            exit()
        else:
            translateAndSend(userInput)
        

if __name__ == '__main__':
    terminal()