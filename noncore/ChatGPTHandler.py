import openai
import threading 
openai.api_key = "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"




    
    
def terminal():
    while True:    
        userInput = input('User:')

        if userInput == 'exit':
            exit(0)
        else:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages = [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": userInput}        
                ]
            )
            print('Terminal:', response.choices[0].message)
                
        
if __name__ == '__main__':
    terminal()
    
    