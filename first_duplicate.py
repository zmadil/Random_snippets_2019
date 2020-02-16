array=[5,4,4,6,5,3,2]
min_index=-1
dic={}

for i in range(len(array)-1,-1,-1):
	if array[i] in dic.keys():
		min_index=i
	else:
		dic[array[i]]=1


if min_index!=-1:
	print('Found ', array[min_index])
else:
	print('Not found')

