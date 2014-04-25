'''
Created on 25 kwi 2014

@author: Gocom
'''
import os
class Prepare:
    '''
    Prepare the base workspace to Joiner
    '''
    

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def __createDir(self, path):      
        '''
        Method to check and create directory
        '''  
        try:
            if not os.path.exists(path):
                os.mkdir(path)            
        except:
            return False
        
        return True
    
    def preparePath(self):
        '''
        Method prepare the base directories
        '''
                
        return self.__createDir('./js_joiner') and self.__createDir('./js_joiner/compress') and self.__createDir('./js_joiner/plain')        
        
    
        