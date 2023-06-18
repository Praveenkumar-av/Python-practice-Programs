# Write a class called Converter. The user will pass a length and a unit when declaring 
# an object from the class—for example, c = Converter(9, 'inches'). The possible 
# units are inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters. 
# For each of these units there should be a method that returns the length converted 
# into those units. For example, using the Converter object created above, the user 
# could call c.feet() and should get 0.75 as the result.

val=int(input('Enter the value :'))
unit=input('Enter the unit :')
class converter :
    def __init__(self,val,unit) :
        self.val=val
        self.unit=unit
    def inches(self) :
        if self.unit=='feet' :
            return 12*self.val
        elif self.unit=='yards' :
            return self.val*36
        elif self.unit=='miles' :
            return self.val*63360
        elif self.unit=='kilometers' :
            return self.val*39370.1
        elif self.unit=='meters' :
            return self.val*39.37
        elif self.unit=='centimeters' :
            return self.val*0.3937
        elif self.unit=='millimeters' :
            return self.val*0.03937
    def feet(self) :
        if self.unit=='inches' :
            return self.val/12
        elif self.unit=='yards' :
            return self.val*3
        elif self.unit=='miles' :
            return self.val*5280
        elif self.unit=='kilometers' :
            return self.val*3280.84
        elif self.unit=='meters' :
            return self.val*3.28084
        elif self.unit=='centimeters' :
            return self.val*0.0328084
        elif self.unit=='millimeters' :
            return self.val*0.00328084
    def yards(self) :
        if self.unit=='inches' :
            return self.val/36
        elif self.unit=='feet' :
            return self.val/3
        elif self.unit=='miles' :
            return self.val*1760
        elif self.unit=='kilometers' :
            return self.val*1093.61
        elif self.unit=='meters' :
            return self.val*1.09361
        elif self.unit=='centimeters' :
            return self.val*0.010936
        elif self.unit=='millimeters' :
            return self.val*0.0010936
    def miles(self) :
        if self.unit=='inches' :
            return self.val/63360
        elif self.unit=='feet' :
            return self.val/5280
        elif self.unit=='yards' :
            return self.val/1760
        elif self.unit=='kilometers' :
            return self.val/1.60934
        elif self.unit=='meters' :
            return self.val/1609.344
        elif self.unit=='centimeters' :
            return self.val/160934.4
        elif self.unit=='millimeters' :
            return self.val/1609344
    def kilometers(self) :
        if self.unit=='inches' :
            return self.val*2.54E-5
        elif self.unit=='feet' :
            return self.val*0.0003038
        elif self.unit=='yards' :
            return self.val*0.0009144
        elif self.unit=='miles' :
            return self.val*1.60934
        elif self.unit=='meters' :
            return self.val/1000
        elif self.unit=='centimeters' :
            return self.val/100000
        elif self.unit=='millimeters' :
            return self.val/1000000
    def meters(self) :
        if self.unit=='inches' :
            return self.val*0.0254
        elif self.unit=='feet' :
            return self.val*0.3048
        elif self.unit=='yards' :
            return self.val*0.9144
        elif self.unit=='miles' :
            return self.val*1609.344
        elif self.unit=='kilometers' :
            return self.val*1000
        elif self.unit=='centimeters' :
            return self.val/100
        elif self.unit=='millimeters' :
            return self.val/1000
    def centimeters(self) :
        if self.unit=='inches' :
            return self.val*2.54
        elif self.unit=='feet' :
            return self.val*30.48
        elif self.unit=='yards' :
            return self.val*91.44
        elif self.unit=='miles' :
            return self.val*160934.4
        elif self.unit=='kilometers' :
            return self.val*100000
        elif self.unit=='meters' :
            return self.val*100
        elif self.unit=='millimeters' :
            return self.val*0.1
    def millimeters(self) :
        if self.unit=='inches' :
            return self.val*25.4
        elif self.unit=='feet' :
            return self.val*304.8
        elif self.unit=='yards' :
            return self.val*914.4
        elif self.unit=='miles' :
            return self.val*1609344
        elif self.unit=='kilometers' :
            return self.val*1000000
        elif self.unit=='meters' :
            return self.val*1000
        elif self.unit=='centimeters' :
            return self.val*10
c=converter(val,unit)
print(c.yards(),'yards')