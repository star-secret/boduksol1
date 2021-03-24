class Class:
	name = ''
    
    def __init__(self, name):
    	self.name = name
    
    def __del__(self):
    	self.name = ''
        
        
abc = Class('paran')
abc.print()