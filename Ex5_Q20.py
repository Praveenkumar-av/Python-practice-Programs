# Write a program that converts a time from one time zone to another. The user enters
# the time in the usual American way, such as 3:48pm or 11:26am. The first time zone
# the user enters is that of the original time and the second is the desired time zone.
# The possible time zones are Eastern, Central, Mountain, or Pacific.
# Time: 11:48pm
# Starting zone: Pacific
# Ending zone: Eastern
# output: 2:48am

time1=input('Enter the time in hh:mm period:')
time1h=int(time1[0:2])  # time1 hour
time1m=int(time1[3:5])  # time1 minutes
period=time1[5:7]       # am or pm
print(time1h,time1m,period)
place1=input('Starting zone :')
place2=input('Ending zone :')
time2h=0
time2m=time1m  # the minutes doesn't change in this scenerio
gmt=0          # gmt hours
stop=0
if place1=='pacific' :
    gmt=time1h+7
elif place1=='eastern' :
    gmt=time1h+4
elif place1=='central' :
    gmt=time1h+5
elif place1=='mountain' :
    gmt=time1h+6
else :
    stop=1
if stop==1 :
    print('Enter a valid zone')
else :
    if place2=='pacific' :
        time2h=gmt-7
    elif place2=='eastern' :
        time2h=gmt-4
    elif place1=='central' :
        time2h=gmt-5
    elif place1=='mountain' :
        time2h=gmt-6
    if 0<=time2h<=12 :
        print('{:02d}:{:02d}{}'.format(time2h,time2m,period))
    else :
        period='pm' if period=='am' else 'am'
        print('{:02d}:{:02d}{}'.format(time2h-12,time2m,period))