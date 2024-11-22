#Dictionary

student = {'name':'fahad', 'age': 23, 'courses': ['data science', 'programming']}

#Updating and adding
student['name'] = 'Ali'
student.update({'last-name': 'jadoon'})


#Deleting
#del student['age']
#age = student.pop('last-name')

#Loop
"""
#key will hold the keys and value will hold the value
for key, value in student.items():#Item method is used to print all items in the list 
    print(key, value)
"""
#printing
"""
1.print(student['courses'])
2. print(student.get('gender','Not fount'))
3. print(student.keys()) #This will print all the keys 
4. print(student.values()) # This will print all the values
5. print(student.items()) #This will print all dictionary
"""

#Nested dictionary
myfamily = { 
    "child1": { "name": "Emil", "year": 2004 }, 
    
    "child2": { "name": "Tobias", "year": 2007 },
    
    "child3": { "name": "Linus", "year": 2011 }
}

#printing nested dictionary
#use the keys of the outer and inner dictionaries without coma between both the keys
print(myfamily['child2']['name']) 