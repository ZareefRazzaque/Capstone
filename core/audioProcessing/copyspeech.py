import textToSpeech
import speechProcesser
import threading



def speechRepeatingFunction():

    def innerfunction(text):
        print(text)
        thread = threading.Thread( target=  textToSpeech.translate, args=(text) )  

        thread.start()
    
    speechProcesser.speechrecognizer(innerfunction)


if __name__ == "__main__":
    speechRepeatingFunction()