import speech_recognition as sr
try: import audioVariables
except: pass

class speechInput():
    '''
    this class deals with microphone input, the init selects an input from the list of available inputs 
    '''
    
    def __init__(self, microphonename = None) -> None:
        
        if microphonename != '' :
            for index, name in enumerate(sr.Microphone.list_microphone_names()):
                if str(name) ==  microphonename:
                    self.microphone = index
                    print("found")
                    break
        else:
            self.microphone =  None 
            print("none was set")
    
    
    def speechrecognizer(self, function):
        '''
        this takes a funciton as an input, 
        takes mic audio and converts it into text and sends it through the inputted function
        '''
        
        recognition = sr.Recognizer()
        
        while True:
            with sr.Microphone(device_index=3) as mic:
                try:
                    audio = recognition.listen(mic)
                    text =  recognition.recognize_google(audio)
                    function(text)
                    
                except sr.UnknownValueError : 
                    print('unkown error')
                    recognition = sr.Recognizer()
        
        
if __name__ == '__main__':
    for index, name in enumerate(sr.Microphone.list_microphone_names()): print(index, name)
    SP = speechInput(audioVariables.recievedFromMic)
    SP.speechrecognizer(print)
