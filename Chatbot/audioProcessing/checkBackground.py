import pyaudio
import speech_recognition as sr
import pygame
import audioVariables

class checkBackground:
    '''this class deals with recording audio and choosing whether it is suitable to talk'''        
    
    def __init__(self, microphonename = None) -> None:
        pass

    
    
    def recordAudio(self, function):
        
        recognition = sr.Recognizer()
        
        
if __name__ == '__main__':
    
    p = pyaudio.PyAudio()
        
    info = p.get_host_api_info_by_index(0)
    numdevices = info.get('deviceCount')

    print("Available audio devices:")
    for i in range(0, numdevices):
        if (p.get_device_info_by_host_api_device_index(0, i).get('maxInputChannels')) > 0:
            print(f"  {i}: {p.get_device_info_by_host_api_device_index(0, i).get('name')}")

    CB = checkBackground(input('(system) enter input device name: '))
        
        