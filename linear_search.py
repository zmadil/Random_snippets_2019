array=[1,4,7,3,23,67]
find=5




def search(list,n):
	for i in range(len(list)):
		if list[i]==n:
			return True
	return False

print(search(array,find))

