
from multiprocessing import Queue
import multiprocessing
import time

try:
    from audioProcessing import textToSpeech, speechInput, audioVariables
except:
    import textToSpeech
    import speechInput
    import audioVariables


class audiohandler :
    def __init__(self) :
        self.TTSQueue =  Queue()
        
        
        
        self.heardQueue = Queue()
        
        
        
    def alexaSpeak(self, text):
        self.TTSQueue.put(text)
    
    def speakFunction(self):
        while True:
            if not self.TTSQueue.empty(): 
                try: textToSpeech.translateAndSend(self.TTSQueue.get())
                except AssertionError: pass
                
                
                
                
                
    def alexaHeard(self):
        self.Input = speechInput.speechInput(audioVariables.recievedFromMic)
        self.Input.speechrecognizer(self.heardFunction)
    
    
    def heardFunction(self, text):
        with open('alexaHeard.txt','w') as file:
            file.write(text)
        
def startAudioProcesses():
    a = audiohandler()
    TTSProcess = multiprocessing.Process(target=a.speakFunction)
    heardProcess = multiprocessing.Process(target=a.alexaHeard)
    TTSProcess.start()
    heardProcess.start()
    return a
        
        

    
def terminal():

    a = startAudioProcesses()
    time.sleep(2)
    while True:
        userInput = input("User: ")
        
        if userInput == 'exit':
            exit()
        else:
            a.alexaSpeak(userInput)
        

if __name__ == '__main__':
    terminal()
    
        

        
        
            
    
    
    