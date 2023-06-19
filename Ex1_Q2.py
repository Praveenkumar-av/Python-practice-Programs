# Write a program to read x, mean, standard deviation, and find the normalized value 
# z=(x-mean)/std

x=float(input('Enter x :'))
mean=float(input('Enter the mean :'))
std=float(input('Enter the standard deviation :'))
z=(x-mean)/std
print('Normalized value :',round(z,2))