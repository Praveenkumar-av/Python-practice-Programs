class temp1 :
    te='abc'
    def __init__(self,s) :
        self.t=s
    def game(self) :
        self.b='chd'

class temp2 :
    def __init__(self) :
        self.a='bcd'
    
c1=temp1('abc')
c2=temp1('xyz')
print(c1)
print(id(c2.te))