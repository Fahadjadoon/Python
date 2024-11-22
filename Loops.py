#The for loop is used to iterate over a sequence 
#(like a list, tuple, dictionary, set, or string).

"""
num = [1,2,3,4,5]

for x in num:
    for y in 'abc':
        print(x, y)
"""

#range
"""
# A range is an inbuild function that runs for the number of time mention in ()
for i in range(1, 10): #we can also add starting number of this loop by adding it before the renge number
    print(i)
"""

#Do-While
x = 0

while x <= 100:
    if x == 50:
        break
    print(x)
    x += 2