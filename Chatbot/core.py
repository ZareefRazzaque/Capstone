import sys
import time
import Chatbot.audioProcessing
import threading
import os

from django.http import HttpResponse

from enum import Enum

from Chatbot.audioProcessing import *
from Chatbot.audioProcessing.AudioHandler import startAudioProcesses


class state(Enum):
    '''this class helps keep track of the state of the system using the subscriber pattern '''
    active = 1
    passive = 2
    waitingForUser = 3
    disabled = 0
    
    subscriberModules = []
    currentState = disabled
    
    
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
    
    
    
'''method for dealing with Internet communcations'''

def personDetected(request):
    '''this is for when a person is detected by the alexa'''
    if state.waitingForUser == state.disabled: return HttpResponse('this is a failed test',status = 500)
    if state.currentState == state.waitingForUser: 
        state.changeCurrentState(state.passive) 
        

def start(request):
    '''this initializes the server so that it is ready'''
    if state.waitingForUser == state.disabled: return HttpResponse('this is a failed test',status = 409)
    
    with open('test.txt','w') as file:
        file.write('i have recieved a request')
    try:
        A = startAudioProcesses()
        time.sleep(2)
        target = 'bedroom'
        return HttpResponse('this is a test',status = 200)
    except Exception: return HttpResponse('this is also a failed test',status = 500)
    
    

    
if __name__ == '__main__':
    A = startAudioProcesses()
    time.sleep(2)
    target = str(input("(System) enter name of target device: "))
    dropIn(target, A)
    

    
    
    

        


    
    
    