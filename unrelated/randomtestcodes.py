import speech_recognition as sr

def testcode(microphonename):
    if microphonename != None :
        print('pass 1')
        for index, name in enumerate(sr.Microphone.list_microphone_names()):
            
            print(name)
            if str(name) ==  microphonename:
                microphone = index
                print("found")
                break
    else: print("none was set")
    
    
    
testcode('CABLE Output (VB-Audio Virtual Cable)')
    
