
list1=[3,5,7,23,4,1]


def target(list1, value):
	
	for i in range(len(list1)):
		
		for j in range(i+1,len(list1)):
			if list1[j]+list1[i] == value:
				print (list1[i],list1[j])
				return True
	else:									#Else statement placing, watch!
		return False

#print(target(list1,30))



def hash_table(list1,value):
	ht=dict()
	for i in range(len(list1)):
		if list1[i] in ht:
			print(ht[list1[i]], list1[i])
			return True
		else:
			ht[value- list1[i]]= list1[i]
	return False

print(hash_table(list1, 5))