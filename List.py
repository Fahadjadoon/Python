#List

cars = ['bmw', 'toyota', 'honda', 'mercedice', 'rollsroles']
cars2 = ['honda X', 'honda city']

cars.append('Ferrari') #this will add the value at the end of the list
cars.insert(1, 'suzuki') #This will insert given value(suzuki) at the mentioned index[1]
cars.extend(cars2) #when we want to add all values of our 2nd lint to 1st list and if we'll insert the list it will only add the lst not it's values

cars.pop() #It removes the last item in the list

cars.reverse() #It will reverse the list

#print(cars)


#Sort method & sorted function

nums = [3, 1, 9, 7, 5]
nums2 = [33, 11, 92, 73, 45]

nums.sort() # It sorts the original list

sorted_func = sorted(nums2) # It makes the copy of the list and sort it

#print(nums)
#print(sorted_func)
#print(9 in nums) # It will print our desire value from the list


# looping the list
"""
#This loop will print out all values in list.
#"num" is the variable which stores the value to be printed.

for num in nums: 
    print(num)

-------------------------

#In this enumerate will also print the index.
#"index" will store index of list and num2 will store current value.

for index, num2 in enumerate (nums2, start=1): 
    print(index, num2) 
"""

#joining the list and making a single string
courses = ['math', 'english', 'science', 'computer']

joined_courses = '-'.join(courses)# It will join the array on basis of whatever string is provided inside ' '...

print(joined_courses)

#Split
#Split will take string as an input and break it down and convert it into a list
#It splits the string according to the delimiter inside ()paranthesis
#If it's empty it will use white spaces to split or (,) it will look for comas in the string
sentence = 'Hello this is my pyhon code'
words = sentence.split()

#print(words)


#Tuples
#Tuples are defined in (pranthesis)
#Tuples is also a list but it cannot be modified and unlike list it dosen't have much methods
Tuple = (1, 2, 3, 4) 