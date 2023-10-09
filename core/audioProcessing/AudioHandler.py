from multiprocessing import Queue
import multiprocessing
import threading
import textToSpeech
import speechInput
import audioVariables


class audiohandler :
    def __init__(self) :
        self.TTSQueue =  Queue()
        self.TTSProcess = multiprocessing.Process(target=self.speakFunction)
        #self.TTSProcess.start()
        
        self.heardQueue = Queue()
        self.heardProcess = multiprocessing.Process(target=self.alexaHeard)
        self.heardProcess.start()
        
    def alexaSpeak(self, text):
        self.TTSQueue.put(text)
    
    def speakFunction(self):
        while True:
            if not self.TTSQueue.empty(): 
                try: textToSpeech.translateAndSend(self.TTSQueue.get())
                except AssertionError: pass
                
                
                
                
                
    def alexaHeard(self):
        self.Input = speechInput.speechInput(audioVariables.SendToAlexa)
        self.Input.speechrecognizer(self.heardFunction)
    
    
    def heardFunction(self, text):
        print(text)
        
        
if __name__ == '__main__':
        a = audiohandler()
        
            
    
    
    