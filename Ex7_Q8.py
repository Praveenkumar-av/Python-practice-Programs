# Consider a class “Dictionary” to represent a dictionary of words defined as a private data member
# and a class “Longest_String” which has a string data member. Write appropriate functions to
# receive the input string and a function “Largest_word” to find the largest word in the dictionary by
# deleting some characters of the given string.
# Input : dict = {"ale", "apple", "monkey", "plea"}
# str = "abpcplea"
# Output : apple
# Input : dict = {"pintu", "geeksfor", "geeksgeeks","forgeek"}
# str = "geeksforgeeks"
# Output : geeksgeeks

class Dictionary :
    def __init__(self,words) :
        self.words=words

class Longest_String(Dictionary) :
    def __init__(self,words,str) :
        self.str=str
        self.result=''
        super().__init__(words)
    def Largest_word(self) :
        len_str=len(self.str)
        min_diff=-1
        for s in self.words :
            diff=0
            len_s=len(s)
            for i in range(len_str) :
                if i<len_s :
                    if s[i]!=self.str[i] :
                        diff+=1
                else :
                    diff+=1
            if min_diff==-1 :
                min_diff=diff
            if diff<min_diff :
                min_diff=diff
                self.result=s
        return self.result

words=eval(input('Enter the list of words :'))
str=input('Enter the string :')
l=Longest_String(words,str)
print(l.Largest_word())