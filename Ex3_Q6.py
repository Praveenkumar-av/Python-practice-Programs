  #6. Implement a lookup table concept (LUT) using python lists. Lookup #table concept is used to
 #retrieve values from the table in fastermanner.
 #Create a list which stores the computations of a function "3x+2" for a range of integer values from 0 to 7
    # 0 1 2  3  4  5  6  7 
    # 2 5 8 11 14 17 20 23
 #Now, use the LUT to access values associated with elements 0 to 7 Create another list which holds 
 #only elements from 0 to 7, refer the lookup table and find the output of computations 
 #Example: If the list is [0,7,6,3,1] then the output is a list [2,23,20,11,6]
  #Additional marks will be provided if the student is able to prove that LUT decreases the amount of 
 #time required for computation when compared with sequential processing of elements.
    #Hint: Use the time module to measure the time taken for computation of the function for a range of
    #values and the time taken for accessing the LUT.

lst=[]
for i in range(8) :
    lst.append(3*i+2)
print(lst)
result=[]
search=eval(input('Enter the list from 0 to 7 to search:'))
for i in search :
    result.append(lst[i])
print('Result :',end='')
print(result)