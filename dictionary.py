

list1= ['geroge', 'tom','emily','jenny','tom']

def appears_twice(list1):
	for i in range(len(list1)):
		for j in range(i+1,len(list1)):
			if list1[j]==list1[i]:
				return True 

print(appears_twice(list1))



