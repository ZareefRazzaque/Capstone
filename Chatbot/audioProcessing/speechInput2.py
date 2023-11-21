import pyaudio
import wave
import numpy as np
import librosa
import audioop
import whisper

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
               
    def speechrecognizer(self, function):
        '''
        this takes a funciton as an input, 
        takes mic audio and converts it into text and sends it through the inputted function
        '''
        model = whisper.load_model("base")
        
        while True:
            self.record()
            audio, sr = librosa.load(f'{audioVariables.audiopath}/speachrecording.wav')
            result = model.transcribe(audio, language = 'en')
            function(result["text"])
        
        
                
    def record(self):
        '''records sound when the threshold for noise reaches past a certian level'''
        print('recording')
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
            
            audioRMS = audioop.rms(audio[-1024:],2)
            
            if audioRMS > 1000 and startedSpeaking == False:
                startedSpeaking = True
                if len(audioFrames) > (44100*2/1024):
                    audioFrames = audioFrames[-int(44100*2/1024):]
            
            if startedSpeaking == True:
                silent = all( audioop.rms(i,2) <= 1000 for i in audioFrames[-int(44100 * 3 / 1024):])
                
                if silent == True:
                    break
            
        with wave.open(f'{audioVariables.audiopath}/speachrecording.wav','wb') as file:
            file.setnchannels(1)
            file.setsampwidth(self.p.get_sample_size(pyaudio.paInt16))
            file.setframerate(44100)
            file.writeframes(b''.join(audioFrames))
            
        audioStream.stop_stream()
        audioStream.close()
        
if __name__ == '__main__' :
    SI = speechInput()
    SI.speechrecognizer(print)