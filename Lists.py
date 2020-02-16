
# Function to find Second largest of numbers in list
'''list1 = [10, 20, 4, 45, 99,34,12,657] 
 
maximum=max(list1[0],list1[1])
secondmax=min(list1[0],list1[1])

for i in range(2,len(list1)):
	if list1[i]>maximum:
		secondmax=maximum
		maximum=list1[i]
	elif list1[i]>secondmax:
		secondmax=list1[i]

print (maximum)
print (secondmax)'''


#function that takes number and converts to list and passes that list to function and find mmax and secondlargest
def find2max(list1):
	
	maximum=max(list1[0],list1[1])
	secondmax=min(list1[0],list1[1])

	for i in range(2,len(list1)):
		if list1[i]>maximum:
			secondmax=maximum
			maximum=list1[i]
		elif list1[i]>secondmax:
			secondmax=list1[i]

	print (maximum)
	print (secondmax)

print('how many')
total=int(input())
list2=[]
for j in range(total):
	print('Enter number ')
	x=int(input())
	list2.append(x)
print(list2)
print('------------------------')
	
find2max(list2)