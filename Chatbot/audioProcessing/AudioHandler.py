
from multiprocessing import Queue
import multiprocessing
import time

try:
    from Chatbot.audioProcessing import textToSpeech, speechInput, audioVariables
except:
    import Chatbot.audioProcessing.textToSpeech
    import Chatbot.audioProcessing.speechInput
    import Chatbot.audioProcessing.audioVariables


class audiohandler :
    '''
    this will be the wrapper interface that should be used for python modules to interact with the audio functions
    this also deals with parallel processes for the audio functions
    '''
    
    def __init__(self) :
        self.TTSQueue =  Queue()
        self.heardQueue = Queue() #unused for now
        
        
    def alexaSpeak(self, text):
        '''this function should be called when the system wishes have alexa speak something '''
        
        self.TTSQueue.put(text)
    
    def speakFunction(self):
        '''a private function that is called to send data to alexas speaker'''
        
        while True:
            if not self.TTSQueue.empty(): 
                try: textToSpeech.translateAndSend(self.TTSQueue.get())
                except AssertionError: pass
                
                
    def alexaHeard(self):
        ''' another private function moving audio heard from the microphone to the heard function'''
        
        self.Input = speechInput.speechInput(audioVariables.recievedFromMic)
        self.Input.speechrecognizer(self.alexaheard)
    
    #TODO
    def alexaheard(self, text):
        with open('alexaHeard.txt','w') as file:
            file.write(text)
        
def startAudioProcesses():
    '''starts the parallel processes for audio'''
    
    a = audiohandler()
    TTSProcess = multiprocessing.Process(target=a.speakFunction)
    heardProcess = multiprocessing.Process(target=a.alexaHeard)
    TTSProcess.start()
    heardProcess.start()
    return a
        
        

def terminal():
    '''terminal for testing purposes'''

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
    
        

        
        
            
    
    
    