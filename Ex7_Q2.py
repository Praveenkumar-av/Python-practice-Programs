# Create a class called Fruit with a method Boolean hasAPeel(). Write another class Vegetable with the
# method Boolean isARoot(). Create a class called Checking which consists of the following methods:
# String doesThisHaveAPeel(Fruit f) and String doesThisHaveARoot(Vegetable v).
# The doesThisHaveAPeel() should in turn check hasAPeel(). If true display “This has a peel”. Else
# display “This doesn’t have a peel”. Similarly the doesThisHaveARoot() should check the isARoot(). If
# yes, display a message “This sis a root” else display “This is not a root”.
# Create a class called Tomato which implements the above classes and provides proper implementation
# for the above methods.

class fruit :
    def __init__(self,name) :
        self.name=name

    def hasAPeel(self) :
        if self.name=='Tomato' :return True
        else :return False
    
class vegetable :
    def __init__(self,name) :
        self.name=name
    
    def isARoot(self) :
        if self.name=='Tomato' :return True
        else :return False 

class checking(fruit,vegetable) :
    def __init__(self) :
        fruit.__init__(self,'Tomato')
        vegetable.__init__(self,'Tomato')

    def doesThisHaveAPeel(self) :
        if self.hasAPeel()==True :
            print('This has a peel')
        else :
            print("This doesn't have a peel")

    def doesThisHaveARoot(self) :
        if self.isARoot()==True :
            print('This  is a Root')
        else :
            print("This is not a Root")

class Tomato(checking) :
    def __init__(self) :
        super().__init__()
    
    def check(self) :
        self.doesThisHaveAPeel()
        self.doesThisHaveARoot()

obj=Tomato()
obj.check()