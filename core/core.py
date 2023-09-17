import audioProcessing

def dropIn(name):
    AudioPrompt = "alexa... drop in on " +name
    audioProcessing.textToSpeech.translate(AudioPrompt)
    
    
if __name__ == '__main__':
    target = str(input("(System) enter name of target device: "))
    dropIn(target)
    