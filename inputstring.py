names_of_cat=[]

print ('How many cats would you like to store?')
x=int(input())

for i in range (0,x):
	print ('Please enter ')
	name=input()
	names_of_cat=names_of_cat + [name]
	if name== '':
		break

print (names_of_cat) 