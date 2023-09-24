import speech_recognition as sr
 
class speechProcessor():
    
    def __init__(self, microphonename = None) -> None:
        
        if microphonename != None :
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                
                print(microphonename, '----', name)
                if name ==  microphonename:
                    self.microphone = index
                    print("found")
                    break
        else: print("none was set")
    
    #this takes a funciton as an input, takes mic audio and converts it into text and sends it through the inputted function
    def speechrecognizer(self, fucntion):
        recognition = sr.Recognizer()
        
        while True:
            try:
                with sr.Microphone(4) as mic:
                    print("ready")
                    audio = recognition.listen(mic)
                
                    text =  recognition.recognize_google(audio)
                    fucntion(text)
                    
            except sr.UnknownValueError : 
                print("something went wrong, restarting the mic")
                recognition = sr.Recognizer()
                continue
        
        
if __name__ == '__main__':
    for index, name in enumerate(sr.Microphone.list_microphone_names()): print(index, name)
    SP = speechProcessor(input('(system) enter input device name: '))
    SP.speechrecognizer(print)
