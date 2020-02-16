string1= ['Math', 'English','Urdu','Science']
print('Please specify the subject you want to find')
a=str(input())

for index,value in enumerate(string1):
	if value==a:
		print ('The index is ' +str(index)+ ' for the subject ' +str(a))
