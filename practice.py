
class SLLList:
    def __init__(self):
        self.first = None 

    def addfirst(self, x):
        
        newnxt = self.first
        self.first = node(x, newnxt)

    def addlast(self, x):
        
        newnode = node(x)
        if not self.first:  
            self.first = newnode
        else:
            current = self.first
            while current.b:  
                current = current.b
            current.b = newnode 
class node:
    def __init__(self, item, nxt=None):
        self.a = item  
        self.b = nxt 
   

l = SLLList()
l.addfirst(15)  
l.addfirst(10)  
l.addfirst(5)   
l.addfirst(1)    
l.addlast(20)
l.addfirst(45)