
#Given 2 arrays, find 2 numbers whose sum matches the target value. Return a bool

arr1=[4,6,43,67,2,1]
arr2=[43,57,22,56,2,4]

#Used a Hashmap. 
#Time Complexity: O(n)
#Space Complexity: O(n) as we are storing structure

def sum_of_two(arr1,arr2,target):
	dic={}
	for i in range(len(arr1)):
		dic[target-arr1[i]]=1
	print(dic)

	for i in range(len(arr2)):
		if arr2[i] in dic:
			return True
	return False

print(sum_of_two(arr1,arr2,5))



	
print('-----------------------------')


#Given 2 arrays, find 2 numbers whose sum matches the target value. Return a bool

arr1=[4,6,43,67,2,1]
arr2=[43,57,22,56,2,4]

#Used a Hashmap. 
#Time Complexity: O(n)
#Space Complexity: O(n) as we are storing structure

def sum_of_two(arr1,arr2,target):
	dic={}
	for i in range(len(arr1)):
		dic[target-arr1[i]]=1
	print(dic)

	for i in range(len(arr2)):
		if arr2[i] in dic:
			return True
	return False

print(sum_of_two(arr1,arr2,5))



	


