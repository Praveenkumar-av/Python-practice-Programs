# Define a class “Input” containing a set member function to receive input of a integer array. Write a
# class “sub-array” consisting of Maximum_subarray function. This function given an array arr[] of N
# integers and an integer K it finds the maximum sub-array sum by flipping signs of at most K array
# elements.
# Input: arr[] = {-6, 2, -1, -1000, 2}, k = 2
# Output: 1010
# We can flip the signs of -6 and -1000, to get maximum subarray sum as 1010
# Input: arr[] = {-1, -2, -100, -10}, k = 1
# Output: 100
# We can only flip the sign of -100 to get 100
# Input: {1, 2, 100, 10}, k = 1
# Output: 113
# We do not need to flip any elements

class Input :
    def __init__(self) :
        self.arr=list(eval(input('Enter the array :')))
        self.k=int(input('Enter the value of k :'))
        self.max_sum=0
    
class sub_array(Input) :

    def Maximum_subarray(self) :
        n=len(self.arr)
        for i in range(self.k) :
            min=self.arr[0]
            index=0
            for j in range(1,n) :
                if self.arr[j]<min :
                    min=self.arr[j]
                    index=j
            self.arr[index]=abs(self.arr[index])
        print(self.arr)
        for n in self.arr :
            if n>0 :
                self.max_sum+=n
        return self.max_sum

max=sub_array()
print(max.Maximum_subarray())