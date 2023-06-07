# Create a class “Message” consisting of a private string data member “information”. Write set and
# get functions for assigning and returning value of the attribute “information”. Define a class called
# “Crypto” consisting of a member functions “Vignere_cipher” to generate the cipher text. The
# vignere_cipher technique uses multiple character keys .Each of the keys encrypts one single
# character. Each character is replaced by a number (A=0, B=1, ...Z=25). After all keys are used,
# they are recycled. For encryption, Formula used : E=(M+K)mod 26
# Plaintext: ATTACKATDAWN
# Key: LEMONLEMONLE
# Ciphertext: LXFOPVEFRNHR
# Define class “Display” to print the cipher text and the plain text (original information).

class message :
    def __init__(self) :
        self.info=''
    
    def inforamtion(self) :
        self.info=input('Enter the message text :')
    
class crypto(message) :
    def __init__(self) :
        super().__init__()
        self.inforamtion()
        self.key=input('Enter the key :')
        self.cipher_text=''
        self.str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.val=dict()
        self.alp=dict()
        for i in range(26) :
            self.val[self.str[i]]=i
        for i in range(26) :
            self.alp[i]=self.str[i]
    
    def vignere_cipher(self) :
        n=len(self.info)
        for i in range(n) :
            self.cipher_text+=self.alp[(self.val[self.info[i]]+self.val[self.key[i]])%26]
        del self.key

class display :
    def disp(self) :
        encrypt=crypto()
        encrypt.vignere_cipher()
        print('Cipher text :',encrypt.cipher_text)
        print('Original text :',encrypt.info)

d=display()
d.disp()