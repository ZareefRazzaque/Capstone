import audioProcessing
import threading



def speechRepeatingFunction():

    def innerfunction(text):
        print(text)
        thread = threading.Thread( target=  audioProcessing.textToSpeech.translate, args=(text,) )  

        thread.start()
    
    audioProcessing.speechProcesser.speechrecognizer(innerfunction)


if __name__ == "__main__":
    speechRepeatingFunction()