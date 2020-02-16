list1=[-1,4,67,45,2]
target=20
length=len(list1)

leftindex=0
rightindex=length-1

for i in range(list1):
	for j in range(list1):
		sum= list1[i]+list1[rightindex]
		if sum > target:
			break
			rightindex-=1
			

