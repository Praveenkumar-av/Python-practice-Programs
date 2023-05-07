# Print the following pattern
# 1 
# 1 1 
# 1 2 1 
# 1 3 3 1         
# 1 4 6 4 1       
# 1 5 10 10 5 1   
# 1 6 15 20 15 6 1

from math import comb
for i in range(0,7) :
    for j in range(0,i+1) :
        print(comb(i,j),end=(' '))
    print()