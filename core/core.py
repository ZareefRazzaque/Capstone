import sys
import time
import audioProcessing
import threading
import os
from enum import Enum

from audioProcessing import *
from audioProcessing.AudioHandler import startAudioProcesses


class state(Enum):
    '''this class helps keep track of the state of the system using the subscriber pattern '''
    active = 1
    passive = 2
    waitingForUser = 3
    
    subscriberModules = []
    currentState = active
    
    
    def changeCurrentState(newState):
        '''changes the state of the system and notifies all modules that are subscribed to it'''
        currentState = newState
        
        for function in state.subscriberModules:
            function()
    
    
    def subscribeToState(notifyFunction):
        '''
        modules call this function first to be notified about state changes, takes a function as an input,
        the inputted function gets called when there is a change to the system state
        '''
        state.subscriberModules.append(notifyFunction)
    


def dropIn(name, A):
    '''
    a simple function to trick the alexa app into dropping in on the target alexa
    '''
    AudioPrompt = "Alexa, drop in on " +name
    A.alexaSpeak(AudioPrompt)
    

    
if __name__ == '__main__':
    A = startAudioProcesses()
    time.sleep(2)
    target = str(input("(System) enter name of target device: "))
    dropIn(target, A)
    
    
    
    
    

        


    
    
    