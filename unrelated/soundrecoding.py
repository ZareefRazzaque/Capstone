import librosa 
import wave
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pyaudio 
import speech_recognition
import noisereduce as nr

p = pyaudio.PyAudio()
audiofile, sr = librosa.load('speachrecording.wav')


something = nr.reduce_noise(y=audiofile, sr=sr)



# Separate magnitude and phase
magnitude, phase = librosa.magphase(something)


with wave.open('test.wav', 'wb') as file:
    file.setnchannels(1)
    file.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    file.setframerate(44100)
    file.writeframes(b''.join(something))
    
plt.show()
