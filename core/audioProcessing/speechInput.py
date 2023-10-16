import speech_recognition as sr
 
class speechInput():
    
    def __init__(self, microphonename = None) -> None:
        
        if microphonename != None :
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                if str(name) ==  microphonename:
                    self.microphone = index
                    print("found")
                    break
        else: print("none was set")
    
    #this takes a funciton as an input, takes mic audio and converts it into text and sends it through the inputted function
    def speechrecognizer(self, function):
        recognition = sr.Recognizer()
        
        while True:
            with sr.Microphone(4) as mic:
                try:
                    print("ready")
                    audio = recognition.listen(mic)
                    text =  recognition.recognize_google(audio)
                    function(text)
                    
                except sr.UnknownValueError : 
                    print("something went wrong, restarting the mic")
                    recognition = sr.Recognizer()
                    recognition.adjust_for_ambient_noise(mic)
        
        
if __name__ == '__main__':
    for index, name in enumerate(sr.Microphone.list_microphone_names()): print(index, name)
    SP = speechInput(input('(system) enter input device name: '))
    SP.speechrecognizer(print)