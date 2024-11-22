#Sets
#Sets are defined in {curly braces}
#Set removes the duplicate values & always change the order when printed

country_set1 = {'hungry', 'USA', 'pakistan', 'england'}
country_set2 ={'France', 'USA', 'UAE', 'Iran'}

print(country_set1.intersection(country_set2))#Same values in both sets
print(country_set1.difference(country_set2))#Different values in both sets
print(country_set1.union(country_set2))#Combine both sets
