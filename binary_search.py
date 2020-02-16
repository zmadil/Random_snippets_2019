list1=[3,5,8,12,67,78,99]

search=67


def binarysearch(list1,search):
	lbound=0
	ubound=len(list1)-1
	
	while lbound<= ubound:
		mid=(lbound+ubound)//2
		if list1[mid] < search:
			lbound=mid+1
		elif list1[mid] > search:
			ubound=mid-1
		elif search==list1[mid]:
			return True
	return False
		
	

	

print(binarysearch(list1,78))




