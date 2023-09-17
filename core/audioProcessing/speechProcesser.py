import speech_recognition as sr
 


def speechrecognizer(fucntion):
    recognition = sr.Recognizer()
    
    while True:
        try:
            with sr.Microphone() as mic:
                print("ready")
                audio = recognition.listen(mic)
            
                text =  recognition.recognize_google(audio)
                fucntion(text)
                
        except sr.UnknownValueError : 
            print("something went wrong, restarting the mic")
            recognition = sr.Recognizer()
            continue
        
        
if __name__ == '__main__':
    speechrecognizer(print)
