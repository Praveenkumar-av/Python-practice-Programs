# Write a class called Time whose only field is a time in seconds. It should have a method 
# called convert_to_minutes that returns a string of minutes and seconds formatted as 
# in the following example: if seconds is 230, the method should return '5:50'. It should 
# also have a method called convert_to_hours that returns a string of hours, minutes, 
# and seconds formatted analogously to the previous method.

t=int(input('Enter the time in seconds :'))
class time :
    def __init__(self,t) :
        self.t=t
        self.secs=0
        self.min=0
        self.hour=0
        self.str=0
    def convert_to_minutes(self) :
        self.min=self.t//60
        self.secs=self.t%60
        self.str='{:0>2d}:{:0>2d}'.format(self.min,self.secs)
        return self.str
    def convert_to_hours(self) :
        self.hour=self.min//60
        self.min=(self.min)%60
        self.str='{:0>2d}:{:0>2d}:{:0>2d}'.format(self.hour,self.min,self.secs)
        return self.str
t1=time(t)
print('Time in min:sec is',t1.convert_to_minutes())
print('Time in hr:min:sec is',t1.convert_to_hours())
