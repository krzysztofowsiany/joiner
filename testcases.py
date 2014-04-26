
import unittest
from Joiner.Joiner import Joiner
from Joiner.Prepare import Prepare
import os

class Test1(unittest.TestCase):
    def test_prepare(self):
        print os.getcwd()
        p = Prepare()
        self.assertTrue(p.preparePath())
        self.assertTrue(os.path.exists('./js_joiner'))
        self.assertTrue(os.path.exists('./js_joiner/compress'))
        self.assertTrue(os.path.exists('./js_joiner/plain'))

    #def test_loadfile(self): 
     #   l = Joiner()               
      #  self.assertEqual(l.getJoined(), '')
       # self.assertTrue(l.export('test.js'), 'Export file')
        #self.assertTrue(os.path.exists('./js_joiner/plain/test.js'), 'Save plain joined file to ./js_joiner/plain/')
        

        
    def test_joinFromConfigFile(self):
        l = Joiner()
        path = 'test_join.js'
        json = l.loadConfigFile('joiner_conf.json')
        
        l.join()
                
        self.assertTrue(l.export(fileName = path), 'Export file to one file')
        self.assertTrue(os.path.exists('./js_joiner/plain/'+path), 'Save plain joined file to ./js_joiner/plain/')
        
        
    def test_joinFromConfigFileCompress(self):
        l = Joiner()
        path = 'test_join.js'
        json = l.loadConfigFile('joiner_conf.json')
        
        l.join()
                
        self.assertTrue(l.compress(fileName = path), 'Export file to one file')
        self.assertTrue(os.path.exists('./js_joiner/plain/'+path), 'Save plain joined file to ./js_joiner/plain/')
 
    def test_NoFileName(self):
        l = Joiner()
        path = 'test_join.js'
        json = l.loadConfigFile('joiner_conf.json')
        
        l.join()
                
        self.assertTrue(l.compress(), 'Export file to one file')
        self.assertTrue(os.path.exists('./js_joiner/plain/'+path), 'Save plain joined file to ./js_joiner/plain/')


if __name__ == '__main__':
    unittest.main()