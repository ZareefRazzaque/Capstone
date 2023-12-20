from multiprocessing import Queue
import multiprocessing

from Chatbot.stateInterface import state
from Chatbot.stateInterface import stateInterface



class brain(stateInterface):
    '''this allows the program to think of questions and responses for the user'''
    def __init__(self):
        self.subscribeToStateChange()
        self.thoughts = []
        
        pass
    
    def subscribeToStateChange(self) -> None:
        state.subscribeToState(self.notifyFunction)
        
    def notifyFunction() -> None:
        pass
    
    def start(self):
        '''this function starts the brain'''
        self.brainProcess = multiprocessing.Process(group=None, target=self.run, name=None,  )
        
        
    def run():
        '''this runs the brain '''
        while True:
            pass
        
    def thinkPrompt(self):
        '''this function will allow the system to generate questions'''
        