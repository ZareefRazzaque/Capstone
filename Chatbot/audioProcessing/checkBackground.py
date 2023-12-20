import pyaudio
import speech_recognition as sr
import wave
import librosa 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import speech_recognition



try:from Chatbot.audioProcessing import audioVariables
except: import audioVariables


class checkBackground:
    '''this class deals with recording audio and choosing whether it is suitable to talk'''        
    
    def __init__(self,):
        self.p = pyaudio.PyAudio()
        numDevices = self.p.get_host_api_info_by_index(0).get('deviceCount')
        
        for i in range(0, numDevices):
            if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                
                if self.p.get_device_info_by_host_api_device_index(0,i).get('name') == 'CABLE-A Output (VB-Audio Cable ':
                    self.deviceNumber = i
                    break
                else: print(self.p.get_device_info_by_host_api_device_index(0,i).get('name'))
                    
        
        
    
    
    def isConnected(self):  
        '''called by the core to check if the alexa has connected via drop in this is done by checking for background noise
        '''
        self.recordAudio()
        backgroundAudio, sr  = librosa.load(f'{audioVariables.audiopath}/recording.wav', sr=44100)
        
        
        connected = False
        for i in backgroundAudio:
            if i > 0.002:
                connected = True
                break
        
        return connected
                
    

    def isSuitableToChat(self):  
        '''records the background audio and determines whether its suitable to start talking
        
        the function first checks the volume of the room to see whether it is too loud to start talking
        
        the function then attempts to see if any sounds can be converted into words to check if people are currently talking in the enviroment

        if either of those occur the system will respond with a false otherwise it will respond with true
        '''
        self.recordAudio()
        suitable = True
        
        BackgroundAudio, sr = librosa.load(f'{audioVariables.audiopath}/recording.wav',sr=44100)
        
        totalrms =0
        rmsValues=librosa.feature.rms(y=BackgroundAudio)[0] 
        for rms in rmsValues:
            totalrms += rms
            
        averageRMS = totalrms/len(rmsValues)
        
        print(averageRMS)
        
        if averageRMS> 0.03:
            suitable = False
            
        recognition = speech_recognition.Recognizer()
        try: 
            words = recognition.recognize_google(f'{audioVariables.audiopath}/recording.wav')
            print("Google Speech Recognition thinks you said " , words)
            suitable = False
            
        except Exception:
            print('nothing was detected')
        
        print(suitable)
        
        
        return suitable
            
    def recordAudio(self):
        '''function for recording background audio'''
        
        audioStream = self.p.open(format = pyaudio.paInt16,
                             channels=1,
                             rate = 44100,
                             frames_per_buffer=1024,
                             input=True,
                             input_device_index= self.deviceNumber
                             )
        
        audioFrames = []
        for i in range(0,int(44100/1024*2)):
            audio = audioStream.read(1024)
            audioFrames.append(audio)
            
        with wave.open(f'{audioVariables.audiopath}/recording.wav','wb') as file:
            file.setnchannels(1)
            file.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
            file.setframerate(44100)
            file.writeframes(b''.join(audioFrames))
            
        audioStream.stop_stream()
        audioStream.close()
        
    
        
if __name__ == '__main__':
    
    p = pyaudio.PyAudio()
        
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("Available audio devices:")
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print(f"  {i}: {p.get_device_info_by_host_api_device_index(0, i).get('name')}")

    cb = checkBackground()
    cb.isSuitableToChat()
    
    
    
        
        