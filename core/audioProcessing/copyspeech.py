import textToSpeech
import core.audioProcessing.speechInput as speechInput
import threading



def speechRepeatingFunction():

    def innerfunction(text):
        print(text)
        thread = threading.Thread( target=  textToSpeech.translate, args=(text) )  

        thread.start()
    
    speechInput.speechrecognizer(innerfunction)


if __name__ == "__main__":
    speechRepeatingFunction()