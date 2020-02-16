#0,1,1,2,3,5,8,13,21

print('Please enter how many numbers you want ')
user=int(input())
print('----------------------------')

a=0
b=1
print(a)
print(b)

for i in range(2,user):
	c=a+b
	a=b
	b=c
	print(c)


	




