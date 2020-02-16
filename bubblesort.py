list1=[5,3,7,22,5,9,1]

def bubblesort(list1):
	for i in range(len(list1)):
		for j in range(i+1,len(list1)):
			if list1[j] < list1[i]:
				temp=list1[j]
				list1[j]=list1[i]
				list1[i]=temp
	return list1

bubblesort(list1)
print(list1)

