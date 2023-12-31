import textToSpeech
import Chatbot.audioProcessing.speechInput as speechInput
import threading


def speechRepeatingFunction():
    '''repeats whats heard through the microphone, mainly for testing purposes'''

    def innerfunction(text):
        print(text)
        thread = threading.Thread( target=  textToSpeech.translate, args=(text) )  

        thread.start()
    
    speechInput.speechrecognizer(innerfunction)


if __name__ == "__main__":
    speechRepeatingFunction()