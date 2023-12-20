import sys
import time
import Chatbot.audioProcessing
import threading
import os
import subprocess
import psutil
import multiprocessing
from django.http import HttpResponse


from Chatbot.audioProcessing import *
from Chatbot.audioProcessing import audioHandler
from Chatbot.Intelligence.brain import brain 

from Chatbot.stateInterface import state

class coreVariables():
    '''important variables needed for this file'''
    alexaExePath = "C:\Program Files\WindowsApps\\57540AMZNMobileLLC.AmazonAlexa_3.25.1177.0_x64__22t9g3sebte08\Alexa.exe"
    B = brain()
    AH = None
    alexaApp = None
    target = 'bedroom'      #name of my alexa device
    
    
def dropIn():
    '''
    a function to trick the alexa app into dropping in on the target alexa
    '''
    for i in range(0,4):
        if coreVariables.AH.checkConnected():
            print('connected')
            
            return
        
        print('not connected')
        AudioPrompt = "Hey Alexa, drop in on " + coreVariables.target
        coreVariables.AH.alexaSpeak(AudioPrompt)
        time.sleep(10)
    
    print('restarting alexaapp')
    
    restartApp()
    time.sleep(10)
    dropIn()
    
    
    
    
def restartApp():
    '''restarts the alexa app when there is a problem'''    
    for process in psutil.process_iter(['pid','name']):
        if process.info['name'] == 'Alexa.exe':
            try:
                alexaApp = psutil.Process(process.info['pid'])
                alexaApp.terminate()
            except Exception:
                print('could not kill the alexa app')
                
            time.sleep(3)
            coreVariables.alexaApp = subprocess.Popen(coreVariables.alexaExePath)
                
                
    
#methods for dealing with Internet communcations
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

#try:
    coreVariables.alexaApp = subprocess.Popen(coreVariables.alexaExePath)
    coreVariables.B.start()
    coreVariables.AH =  audioHandler.startAudioProcesses()
    
    target = 'bedroom'
    time.sleep(10)

    return HttpResponse('server is now active',status = 200)
#except Exception as e: 
#    print(e)
#    return HttpResponse(f'server has failed ',status = 500)
    
    

    
if __name__ == '__main__':
    A = startAudioProcesses()
    time.sleep(2)
    target = str(input("(System) enter name of target device: "))
    dropIn()
    
