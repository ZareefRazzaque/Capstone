import audioProcessing
import pyaudio

def dropIn(name):
    AudioPrompt = "alexa, drop in on " +name
    audioProcessing.textToSpeech.translateAndSend(AudioPrompt)
    
    
if __name__ == '__main__':
    target = str(input("(System) enter name of target device: "))
    dropIn(target)
    audioProcessing.textToSpeech.terminal()