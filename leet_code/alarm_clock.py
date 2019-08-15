# You're exhausted after a long day but you still have to set the alarm clock.
# You already have one you set the day before to setTime, so all you have to do is 
# update it.

# To set your alarm, you can scroll through hours and minutes upwards or downwards. 
# One shift changes an hour or minute value by one. The values are organized 
# cyclically, which means that dragging 0 minutes downwards turns it into 59, 
# and dragging 59 upwards turns it into 0 (similarly, 0 hours can become 23 
# in one shift and vice versa).

# You want to set the alarm clock without any extra effort, so you need to 
# calculate the minimum number of shifts required to turn setTime into timeToSet.

# Example:
# alarmClock("07:30", "08:00") = 31.
# alarmClock("23:45", "08:00") = 24


def alarmClock(setTime, timeToSet):
    clicks = 0
    # parse times
    h1,m1 = setTime.split(":")
    h2,m2 = timeToSet.split(":")
    print(h1,h2,m1,m2)
    # determine hour clicks
    hour_diff = abs(int(h1) - int(h2))
    if hour_diff > 12:
        hour_diff = 24 - hour_diff

    clicks += hour_diff

    # determine min clicks
    min_diff = abs(int(m1) - int(m2))
    if min_diff > 30:
        # if mins, add 60 to assist with substraction
        min_diff = 60 - min_diff

    clicks += min_diff

    #clicks = absolute value of min1 - min2
    return clicks

setTime = "07:30" 
timeToSet = "08:00"
print(alarmClock(setTime, timeToSet))

setTime = "23:45" 
timeToSet = "08:00"
print(alarmClock(setTime, timeToSet))