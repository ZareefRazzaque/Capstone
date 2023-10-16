import sys
import audioProcessing
import threading
import os

from audioProcessing import *
from audioProcessing.AudioHandler import audioHandler

def dropIn(name, AH):
    AudioPrompt = "Alexa, drop in on " +name
    AH.alexaSpeak(AudioPrompt)
    
    
if __name__ == '__main__':
    AH = AudioHandler.audioHandler()
    target = str(input("(System) enter name of target device: "))
    dropIn(target)
    
    
    
    
    
    

        


    
    
    