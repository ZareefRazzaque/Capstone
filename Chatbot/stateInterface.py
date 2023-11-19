

class state():
    '''this class helps keep track of the state of the system using the subscriber pattern '''
    active = 1
    passive = 2
    waitingForUser = 3
    disabled = 0
    
    subscriberModules = []
    currentState = disabled
    
    
    def changeCurrentState(newState):
        '''changes the state of the system and notifies all modules that are subscribed to it'''
        currentState = newState
        
        for function in state.subscriberModules:
            function()
    
    
    def subscribeToState(notifyFunction):
        '''
        modules call this function first to be notified about state changes, takes a function as an input,
        the inputted function gets called when there is a change to the system state
        '''
        state.subscriberModules.append(notifyFunction)
    


class stateInterface:
    
    def notifyFunction() -> None:
        '''function for when the system changes state'''
    
    def subscribeToStateChange() -> None:
        ''' subscribes to notif changes'''
        