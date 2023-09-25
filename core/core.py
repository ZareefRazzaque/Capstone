import audioProcessing
import threading
import os

def dropIn(name):
    AudioPrompt = "Alexa, drop in on " +name
    audioProcessing.textToSpeech.translateAndSend(AudioPrompt)
    
    
if __name__ == '__main__':
    SP = audioProcessing.speechProcesser.speechProcessor('CABLE Output (VB-Audio Virtual Cable)')
    target = str(input("(System) enter name of target device: "))
    dropIn(target)
    
    
    T2SThread = threading.Thread(target = audioProcessing.textToSpeech.terminal)
    S2TThread = threading.Thread(target = SP.speechrecognizer, args=(audioProcessing.textToSpeech.translate,))
    
    T2SThread.start()
    S2TThread.start()

        


    
    
    