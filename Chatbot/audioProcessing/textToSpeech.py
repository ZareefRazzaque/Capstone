from pygame import mixer
import os
import threading
from gtts import gTTS

try:
    from Chatbot.audioProcessing.audioVariables import audiopath, sendToSpeaker
except ModuleNotFoundError:
    from audioVariables import audiopath, sendToSpeaker


lock = threading.Lock()

def  translateAndSend(text):
    '''this function deals with converting text into speech along with sending it off to alexa'''

    try:mixer.init(devicename = sendToSpeaker)       #virtual cable allows audio to be heard by alexa app
    except: pass
    
    with lock:                                                          
        speach = gTTS(text)                                                 # we are using google's tts here (does the job for now) #TODO
        speach.save(audiopath+'\\temp.mp3')               #saving file so it can be read
        
        mixer.music.load(audiopath +'\\temp.mp3')          #loading and playing audio here
        mixer.music.play()
    
        while mixer.music.get_busy(): pass                                  #closing the mixer so that the audio file may be deleted
        mixer.music.stop()
        mixer.quit()
        os.remove(audiopath+'\\temp.mp3')               
        

def translate(text):
    '''converts text to tts audio file (for testing purposes)'''
    
    try:mixer.init()       
    except: pass
    path = os.getcwd()
    
    audio = gTTS(text)   
    audio.save(audiopath+'\\temp.mp3')
        
    mixer.music.load(audiopath+'\\temp.mp3')
    mixer.music.play()
    
    while mixer.music.get_busy():pass
    mixer.music.stop()
    mixer.quit()
    
    
    
    

def multithreadedTTS(text):
    '''this function allows for multiple texts to be inputted while the TTS is currently running
    it is probably wise to avoid using this and instead work with translate for more control'''
    print(text)
    thread = threading.Thread( target= translateAndSend, args=(text,) )  

    thread.start()



def terminal():
    '''for testing purposes, creates a terminal for text to be translated into speach'''
    while True:
        userInput = input("User: ")
        
        if userInput == 'exit':
            exit()
        else:
            translate(userInput)
        

if __name__ == '__main__':
    terminal()