# Write a class called Password_manager. The class should have a list 
# called old_passwords that holds all of the user's past passwords. The last item of the 
# list is the user's current password. There should be a method called get_password that 
# returns the current password and a method called set_password that sets the user's 
# password. The set_password method should only change the password if the 
# attempted password is different from all the user's past passwords. Finally, create a 
# method called is_correct that receives a string and returns a 
# boolean True or False depending on whether the string is equal to the current 
# password or not.

class password_manager :
    def __init__(self) :
        self.old_passwords=['1234']
        new_password=''
    def get_password(self) :
        return self.old_passwords[len(self.old_passwords)-1]
    def set_password(self) :
        new_password=input('Enter the new passsword :')
        if new_password in self.old_passwords :
            print('Password already exists! Enter a new password')
        else :
            self.old_passwords.append(new_password)
    def is_correct(self) :
        new_password=input('Enter the current password :')
        if new_password==self.old_passwords[len(self.old_passwords)-1] :
            return True
        else  :
            return False
p=password_manager()
print('Current password :',p.get_password())
p.set_password()
print(p.is_correct())
