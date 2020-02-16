
def selecsort(num):
	
	for i in range(len(num)-1):
		minposition=i 
		for j in range(i+1,len(num)):
			if num[j] < num[i]:
				temp = num[j]
				num[j]= num[i]
				num[i]= temp
			else:
				minposition=j



num = [3,5,7,23,61,90,100,2]
selecsort(num)
print (num)