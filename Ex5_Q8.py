# At a certain school, student email addresses end with @student.college.edu, while 
# professor email addresses end with @prof.college.edu. Write a program that first 
# asks the user how many email addresses they will be entering, and then has the user 
# enter those addresses. After all the email addresses are entered, the program should 
# print out a message indicating either that all the addresses are student addresses or 
# that there were some professor addresses entered.

lst=[]
n=int(input('Enter the no. of emails :'))
p=0
s=0
for i in range(n) :
    lst.append(input('Enter the email :'))
for i in range(n) :
    if lst[i].endswith('@student.college.edu') :
        s+=1
    elif lst[i].endswith('@prof.college.edu') :
        p+=1
if s>0 and p==0 :
    print('All the emails are student addresses')
elif s>0 and p>0 :
    print('There were professor emails entered')
