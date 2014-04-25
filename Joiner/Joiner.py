'''
Created on 25 kwi 2014

@author: Gocom
'''
import os
import json

class Joiner(object):
    '''
    classdocs
    '''       

    def __init__(self):
        '''
        Constructor
        '''
        self.__basePath = './js_joiner/'
        self.__plainPath = os.path.join(self.__basePath, 'plain')
        self.__compressPath = os.path.join(self.__basePath, 'compress')
        self.__joined=''
    
    def __loadFile(self, fileName):
        '''
        Private methot loading the file and return it content
        
        @type fileName: String
        @param fileName: The file name witch are loaded
        
        @rtype: String
        @return: Return the loaded content 
        '''
        content=''
        if os.path.isfile(fileName):
            with open(fileName, 'r') as f:     
                content = f.read()           
            
        return content
    
    def __append(self, fileName):
        '''
        Private method append the loaded file into private variable 
        (join file content in variable)
        
        @type fileName: String
        @param fileName: The name of file witch are appened in to joined content         
        '''
        self.__joined += self.__loadFile(fileName) +'\n'
        
    
    
    def getJoined(self):
        '''
        Public methot returned the joined content
        
        @rtype: String
        @return: Returning the content of current appened file
        '''
        return self.__joined
    
    def export(self, fileName):
        '''
        Public method whitch export the joined content to specific file
        
        @type fileName:String 
        @param fileName:Name of file where are saved the joined content
        
        @rtype: Boolean
        @return: Return the succesed (True) or not (False) of the export operation
         
        '''
        with open(os.path.join(self.__plainPath, fileName), 'w') as f:         
            f.write(self.__joined)                    
            return True
        return False
    
    def join(self):
        '''
        Public method, get the file name from configuration file and append it to joined connted        
        '''
        for f in self.__config['files']:
            self.__append(f)       
        
    
    def loadConfigFile(self, configFile):
        '''
        Public method witch are loading the configuration file (JSON)
        @type configFile: String
        @param configFile: Path of config file
        
        @rtype: Dictionary
        @return: Return the JSON accesable structure (Dict, List, ...)
          
        '''
        
        with open(configFile) as json_file:
            self.__config = json.load(json_file)
        return self.__config
    
    def __runCompress(self, fileName):
        '''
        Private method witch are compress the exported plain file, and store it at new name. 
        The new name are make from file name and after it add the "commpres.".
        
        @type fileName: String
        @param fileName: Name of the plain exported file, this file is base of the compress file.
        
        @rtype: Boolean
        @return: On success are returned True other return False  
        
        '''
        try:
            os.system("java.exe -jar yuicompressor-2.4.8.jar --type js -o {of} {f}".format(
                                                                             of=os.path.join(self.__compressPath, 'compress.' + fileName),
                                                                             f=os.path.join(self.__plainPath, fileName) 
                                                                             ) 
                  )
            return True
        except:
            return False
    
    def compress(self, fileName):
        '''
        Public method, doing the plain export and after that, compress the exported file 
        @type fileName:String
        @param fileName:File name of the exported file
        
        @rtype: Boolean
        @return: Return the success (True) or not (False) of this operation
        '''
         
        if self.export(fileName):
            return self.__runCompress(fileName)
        else:
            return False
        
    
    
    
        