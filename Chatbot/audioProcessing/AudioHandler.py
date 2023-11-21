
from multiprocessing import Queue
import multiprocessing
import time

try:
    from Chatbot.audioProcessing import textToSpeech
    from Chatbot.audioProcessing import speechInput2 
    from Chatbot.audioProcessing import audioVariables
    from Chatbot.audioProcessing import checkBackground
except Exception as  e:
    import textToSpeech, speechInput2, audioVariables, checkBackground
    


class audioHandler :
    '''
    this will be the wrapper interface that should be used for python modules to interact with the audio functions
    this also deals with parallel processes for the audio functions
    '''
    
    def __init__(self) :
        self.TTSQueue =  Queue()
        self.heardQueue = Queue() #unused for now
        self.CB = checkBackground.checkBackground()
        
        
    def alexaSpeak(self, text):
        '''this function should be called when the system wishes have alexa speak something '''
        
        self.TTSQueue.put(text)
    
    def speakFunction(self):
        '''a private function that is called to send data to alexas speaker'''
        
        while True:
            if not self.TTSQueue.empty(): 
                try: textToSpeech.translateAndSend(self.TTSQueue.get())
                except AssertionError: pass
                
                
    def alexaHearing(self):
        ''' another private function moving audio heard from the microphone to the heard function'''
        
        SP = speechInput2.speechInput()
        SP.speechrecognizer(self.alexaHeard)
    
    
    
    def alexaHeard(self, text):
        '''this function deals with when alexa hears something '''
        with open('alexaHeard.txt','a') as file:
            file.write(f'\n {text}')
            file.close()
        
    
    
    def checkTalkingSuitability(self):
        '''returns whether the environment is suitable for chatting in'''
        return self.CB.isSuitableToChat()
    
    
    
    def checkConnected(self):
        '''checks whether the alexa has connected to the program'''
        '''calls the check background class to check if audio is connected'''
        return  self.CB.isConnected()
    
        
        

def terminal():
    '''terminal for testing purposes'''

    time.sleep(2)
    while True:
        userInput = input("User: ")
        
        if userInput == 'exit':
            exit()
        else:
            a.alexaSpeak(userInput)
        

if __name__ == '__main__':
    terminal()
    
        

        
        
            
    
    
    