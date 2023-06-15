class IllegalSentenceException(Exception) :
    pass
class IllegalWordException(Exception) :
    pass
class English :
    def __init__(self) :
        pass
    def getASentence(self,word) :
        try :
            if len(word)>10 or not word[len(word)-1].isalpha() :
                raise IllegalSentenceException()
        except IllegalSentenceException :
            print('IllegalSentenceException')
    def getAWord(self,word) :
        try :
            for ch in word :
                if not ch.isalpha() :
                    raise IllegalWordException()
        except IllegalWordException :
            print('IllegalWordException')

class getInput(English) :
    def __init__(self,word) :
        self.word=word
    def check(self) :
        self.getASentence(self.word)
        self.getAWord(self.word)

word=input('Enter the word :')
obj2=getInput(word)
obj2.check()
