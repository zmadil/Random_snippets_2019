arr=[1,2,2,3,3,3,5,5,5]

hashmap={}

for i in range(len(arr)):
	hashmap.setdefault(arr[i],0)
	hashmap[arr[i]]=hashmap[arr[i]]+1
array=[]
for i in hashmap.values():
	array.append(i)

for i in range(len(array)-1):
	if array[i]==array[i+1]:
		print('Not unique')
	



print(hashmap)