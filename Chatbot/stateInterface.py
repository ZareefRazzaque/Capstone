

from core import state

class stateInterface:
    
    def notifyFunction() -> None:
        '''function for when the system changes state'''
        pass
    
    def subscribeToStateChange() -> None:
        ''' subscribes to notif changes'''
        