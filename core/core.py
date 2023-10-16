import sys
import time
import audioProcessing
import threading
import os

from audioProcessing import *
from audioProcessing.AudioHandler import startAudioProcesses

def dropIn(name, A):
    AudioPrompt = "Alexa, drop in on " +name
    A.alexaSpeak(AudioPrompt)
    
    
if __name__ == '__main__':
    A = startAudioProcesses()
    time.sleep(2)
    target = str(input("(System) enter name of target device: "))
    dropIn(target, A)
    
    
    
    
    
    

        


    
    
    