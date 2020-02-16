courses= ['English', 'Urdu' , 'Math']
courses1= ['Angraizi', 'hindi']

courses.extend(courses1)  #extends extend 1 list and end
print (courses)
print(courses.index('Urdu')) #look for index of a string


for subject in courses:
	print (subject)

for index, course in enumerate(courses, start=1):  #enumerate lets you print index
	print(index,course)


#Tuples not mutable. use () brackets
#sets use {} brackets
#-------------
