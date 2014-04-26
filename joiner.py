#!/usr/bin/env python 

from Joiner.Joiner import Joiner
from optparse import OptionParser

if __name__ == '__main__':
    parser = OptionParser(usage="%prog [-d] destination_file [-c] config_file", version="%prog 0.1")
    parser.add_option("-d", "--destination", dest="filename", help="Destination of output joined file.")
    parser.add_option("-c", "--config", dest="config", help="Specific the config file, default file are joiner_conf.json.")
    parser.add_option("-x","--compress",  action="store_true", dest="compress", help="Commpres the joined files.")
    
    
    (option ,args) = parser.parse_args()
    
    if option.config:
        config = option.config
    else:
        config = 'joiner_conf.json'
    
    l = Joiner()       
    l.loadConfigFile(config)
    l.join()      
    
    if option.filename:        
        if option.compress:
            l.compress(fileName = option.filename)
        else:    
            l.export(fileName = option.filename)
    else:
        if option.compress:
            l.compress()
        else:    
            l.export()
    
