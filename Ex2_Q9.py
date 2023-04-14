  #9. Write a program that prints out the sine and cosine of the angles ranging from 0 to 345° in 15° 
 # increments. Each result should be rounded to 4 decimal places.

import math
for i in range(0,346,15) :
    print(i,'--- %.4f %.4f' %(math.sin(math.radians(i)),math.cos(math.radians(i))))