
finallist=[]
print('Please enter how many numbers the numbers') 
length=int(input())
print('Please enters numbers')
for i in range(length):
	number=int(input())
	finallist=finallist +[number]
print(finallist)


[34, 9, 1, 999, 324, 4]

def secondlargest(list1):
	secondlargest=list1[0]
	largest=list1[1]

	for i in range(2,len(list1)):
		if list1[i] > largest:
			secondlargest=largest
			largest=list1[i]
		elif list1[i] <largest:
			secondlargest=list1[i]

	print('List is ')
	print (list1)
	print('Values are :')
	print(secondlargest)
	print (largest)

secondlargest(finallist)