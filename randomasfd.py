array1=[4,5,7,78,90]
target=85


def targetsum(array1,target):
	for i in range(len(array1)):
		for j in range(i+1,len(array1)):
			if array1[j] + array1[i] == target:
				return(True)
				print ('at indices '+ str(j) + ' and ' + str(i))
				
				
	return(False)
			


print(targetsum(array1,target))