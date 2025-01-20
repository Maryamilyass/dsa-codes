class girl:
    def __init__(self,lover):
        self.lover = lover
    def mylove(self):
        return f"I love {self.lover}"
        
    

maryam = girl("Ahmad")
love = maryam.mylove()
print(love)