  # 9. Accept a list of donors and their information (name, blood type, age) and maintain it as a dict with blood type 
 # as the key value There will be more than one donor. Hence, the details of the donors are maintained as list of tuples. 
 # Each tuple corresponds to one donor which stores the information in a particular order (name, blood type,age)
 # Accept a patient detail in particular the blood type and the age.Print the most compatible donor who should have
 # the same blood type and small age difference. Also print other compatible donors which is a list of donors with same
 # blood type sorted by age difference.

n1=int(input('Enter no. of records :'))
donor=dict()
for i in range(n1) :
    blood=input('Enter the blood group :')
    name=[]
    age=[]
    print('Enter the no. of persons with blood group',blood,':')
    n2=int(input())
    for j in range(n2) :
        name.append(input('Enter the name :'))
        age.append(int(input('Enter the age of the person :')))
        print()
    donor[blood]=(tuple(name),tuple(age))
name=input('Enter the patient name :') # patient name 
blood=input('Enter the blood group of the patient :') # patient blood group
age=int(input('Enter the patient age :')) # patient age
lst1=list(donor[blood][0]) # name of the donors
lst2=list(donor[blood][1]) # age of the donors
lst3=[]  # difference of age
for i in lst2 :
    lst3.append(abs(age-i))
l=len(lst1) # no. of donors
i=0
j=0
while(i<l) :
    j=i+1
    while(j<l) :
        if (lst3[j]<lst3[i]) :
            temp=lst3[j]  # differance of age
            lst3[j]=lst3[i]
            lst3[i]=temp

            temp=lst1[j]  # name
            lst1[j]=lst1[i]
            lst1[i]=temp

            temp=lst2[j]  # age
            lst2[j]=lst2[i]
            lst2[i]=temp
        j+=1
    i+=1
donor[blood]=(tuple(lst1),tuple(lst2))
print(donor[blood])
print('The most copatible donor is :',lst1[0])
print('Other compatible donor :',lst1[1::])