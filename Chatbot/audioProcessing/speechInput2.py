import pyaudio
import wave
import numpy
import librosa

try: from Chatbot.audioProcessing import audioVariables
except: import audioVariables

class speechInput():
    def __init__(self,):
        self.p = pyaudio.PyAudio()
        numDevices = self.p.get_host_api_info_by_index(0).get('deviceCount')
        
        for i in range(0, numDevices):
            if (self.p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
                
                if self.p.get_device_info_by_host_api_device_index(0,i).get('name') == 'CABLE-A Output (VB-Audio Cable ':
                    self.deviceNumber = i
                    break
                else: print(self.p.get_device_info_by_host_api_device_index(0,i).get('name'))
               
               
                
    def record(self):
        '''records audio'''
        audioStream = self.p.open(format = pyaudio.paInt16,
                             channels=1,
                             rate = 44100,
                             frames_per_buffer=1024,
                             input=True,
                             input_device_index= self.deviceNumber
                             
                             )
        
        audioFrames = []
        startedSpeaking = False
        
        while True:
            audio = audioStream.read(1024)
            audioFrames.append(audio)
            
            audioRMS = librosa.feature.rms(audioFrames)
            
            if audioRMS[-1] > 0.1
            
            
        with wave.open(f'{audioVariables.audiopath}/recording.wav','wb') as file:
            file.setnchannels(1)
            file.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
            file.setframerate(44100)
            file.writeframes(b''.join(audioFrames))
            
        audioStream.stop_stream()
        audioStream.close()