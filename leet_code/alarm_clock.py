# You're exhausted after a long day of baking a Christmas turkey and heading to bed, 
# but you still have to set the alarm clock on your iPhone to timeToSet. 
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

# For setTime = "07:30" and timeToSet = "08:00", the output should be
# alarmClock(setTime, timeToSet) = 31.

# Shifting hours upwards once will change the alarm to "08:30", and 
# shifting minutes 30 times downwards will change it to "08:00".

# For setTime = "23:45" and timeToSet = "08:00", the output should be
# alarmClock(setTime, timeToSet) = 24.

# You can shift hours upwards 9 times to change the alarm to "08:45", and 
# shift minutes upwards 15 times to change it to "08:00".

# Input/Output
# [execution time limit] 4 seconds (py3)
# [input] string setTime

# Time your alarm clock is set to in the "hh:mm" format.

# Guaranteed constraints:
# 0 ≤ hh ≤ 23,
# 0 ≤ mm ≤ 59.

# [input] string timeToSet

# Time you want to set alarm to given in the same format as setTime.

# Guaranteed constraints:
# 0 ≤ hh ≤ 23,
# 0 ≤ mm ≤ 59.

# [output] integer

# The minimum number of shifts required to change setTime to timeToSet.
# [Python3] Syntax Tips


def alarmClock(setTime, timeToSet):
    clicks = 0
    # parse times
    h1,m1 = setTime.split(":")
    h2,m2 = timeToSet.split(":")
    print(h1,h2,m1,m2)
    # determine hour clicks
    hour_diff = abs(int(h1) - int(h2))
    if hour_diff > 6:
        hour_diff = 12 - hour_diff

    clicks += hour_diff

    # determine min clicks
    min_diff = abs(int(m1) - int(m2))
    if min_diff > 30:
        # if mins, add 60 to assist with substraction
        min_diff = 60 - min_diff

    clicks += min_diff

    #clicks = absolute value of min1 - min2
    return clicks

setTime = "09:30" 
timeToSet = "01:00"
print(alarmClock(setTime, timeToSet))

setTime = "08:00" 
timeToSet = "01:45"
print(alarmClock(setTime, timeToSet))