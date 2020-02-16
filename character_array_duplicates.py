c_array= 'abcddegffhjko'

unique_list=[]

for i in c_array:
	if i in unique_list:
		pass
	else:
		unique_list.append(i)


print(unique_list)