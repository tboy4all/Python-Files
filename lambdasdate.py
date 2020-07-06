# add = lambda x,y: x + y
# double = lambda val: 2 * val
# yell = lambda str: str.upper() + "!!!"

# add(1,2) # 3
# double(5) # 10
# yell("hello") # 'HELLO!!!'



# from functools import reduce
# a = [1,2,3,4,5]

# reduce(lambda x,y:x+y, a) # 15

# list(map(lambda x:x*2, a)) # [2,4,6,8,10]
# list(filter(lambda x:x*2 > 5, a)) # [3,4]

import datetime

# times
# hour, minute, second
t = datetime.time(1, 25, 10)
t.hour
t.microsecond

print(datetime.time.min)

today = datetime.date.today()
#today.timetuple()
print(today.day)
