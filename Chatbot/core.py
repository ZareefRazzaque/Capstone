import sys
import time
import Chatbot.audioProcessing
import threading
import os
import subprocess

from django.http import HttpResponse


from Chatbot.audioProcessing import *
from Chatbot.audioProcessing.AudioHandler import startAudioProcesses
from Chatbot.Intelligence.brain import brain 

from Chatbot.stateInterface import state

class coreVariables():
    '''important variables needed for this file'''
    alexaExePath = "C:\Program Files\WindowsApps\\57540AMZNMobileLLC.AmazonAlexa_3.25.1177.0_x64__22t9g3sebte08\Alexa.exe"
    B = brain()
    A = startAudioProcesses()
    target = 'bedroom'      #name of my alexa device
    
    
def dropIn():
    '''
    a simple function to trick the alexa app into dropping in on the target alexa
    '''
    AudioPrompt = "Hey Alexa, drop in on " + coreVariables.target
    coreVariables.A.alexaSpeak(AudioPrompt)
    
    
    
'''method for dealing with Internet communcations'''
def DoDropin():
    '''goes straight in to communication with the user'''
    if state.waitingForUser == state.disabled: return HttpResponse('this is a failed test',status = 500)
    if state.currentState == state.active : return HttpResponse('connection already active',status = 409)

    dropIn()

def personDetected(request):
    '''this is for when a person is detected by the alexa'''
    if state.waitingForUser == state.disabled: return HttpResponse('this is a failed test',status = 500)
    if state.currentState == state.waitingForUser: 
        state.changeCurrentState(state.passive) 
        

def start(request):
    '''this initializes the server so that it is ready'''
    
    if state.currentState != state.disabled: 
       return HttpResponse('server is already running',status = 409)

    try:
        subprocess.Popen(coreVariables.alexaExePath)
        
        coreVariables.B.start()
        target = 'bedroom'
        time.sleep(10)
        dropIn()
    
        return HttpResponse('server is now active',status = 200)
    except Exception as e: 
        print(e)
        return HttpResponse(f'server has failed ',status = 500)
    
    

    
if __name__ == '__main__':
    A = startAudioProcesses()
    time.sleep(2)
    target = str(input("(System) enter name of target device: "))
    dropIn()
    
