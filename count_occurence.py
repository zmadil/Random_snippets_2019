arr=[1,4,65,4,2,3,65,1]

hashmap={}
'''
for i in range(len(arr)):
	hashmap.setdefault(arr[i],0)
	hashmap[arr[i]]=hashmap[arr[i]]+1

print (hashmap)
'''

for i in range(len(arr)):
	if arr[i] in hashmap:
		hashmap[arr[i]]=hashmap[arr[i]]+1
	else:
		hashmap[arr[i]]=1

print (hashmap)