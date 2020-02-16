string1= 'My name are is Zain and Adil and I am are and 50 is years old'
split_string= string1.split(' ')
final_string=[]

for i in split_string:
	if i not in final_string:
		final_string.append(i) 

print (final_string)
