arr=[1,2,2,3,3,3,5,5,5]

hashmap={}

for i in range(len(arr)):
	#hashmap.setdefault(arr[i],0)
	#hashmap[arr[i]]=hashmap[arr[i]]+1
	if arr[i] in hashmap:
		hashmap[arr[i]]+=1
	else:
		hashmap[arr[i]]=1

print(hashmap)
#print (len(hashmap.values()))
#print (len(set(hashmap.values())))


if len(hashmap.values())== len(set(hashmap.values())):
	print ('Unique')
else:
	print ('Not Unique')


