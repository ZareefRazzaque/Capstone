import audioProcessing
import threading
import os

def dropIn(name):
    AudioPrompt = "alexa, drop in on " +name
    audioProcessing.textToSpeech.translateAndSend(AudioPrompt)
    
    
if __name__ == '__main__':
    SP = audioProcessing.speechProcesser.speechProcessor('CABLE-A Output (VB-Audio Cable , MME (2 in, 0 out)')
    target = str(input("(System) enter name of target device: "))
    dropIn(target)
    
    
    T2SThread = threading.Thread(target = audioProcessing.textToSpeech.terminal)
    S2TThread = threading.Thread(target = SP.speechrecognizer, args=(print,))
    

    S2TThread.start()
        


    
    
    