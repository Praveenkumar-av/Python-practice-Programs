  #3.	Chef is currently working for a secret research group called NEXTGEN. While the rest of the world 
 #is still in search of a way to utilize Helium-3 as a fuel, NEXTGEN scientists have been able to achieve 2
 #major milestones
 #    •	Finding a way to make a nuclear reactor that will be able to utilize Helium-3 as a fuel
 #    •	Obtaining every bit of Helium-3 from the moon's surface
 #Moving forward, the project requires some government funding for completion, which comes under one condition: to prove its worth, the project should power Chefland by generating at least A units of power each year for the next B years. Help Chef determine whether the group will get funded assuming that the moon has X grams of Helium-3 and 1 gram of Helium-3 can provide Y amount of power.
 #Given A, B, X and Y , determine whether the group will get funded.

A=int(input('Enter the power of each year :'))
B=int(input("Enter the no. of years :"))
X=int(input('Enter quantity of Helium-3 in grams :'))
Y=int(input('Enter the amount of power in each gram :'))
if (A*B<X*Y) :
    print("The group will get fund")
else :
    print('The group will not get fund')