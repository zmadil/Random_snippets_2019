list1='sdfagsdbciourt'
vowels=('a','e','i','o','u')

for i in list1:
	if i in vowels:
		list1=list1.replace(i,'')

print(list1)
