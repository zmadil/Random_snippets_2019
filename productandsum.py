n= 2566
print(type(n))
x=list(map(int,str(n)))
result1=1
result2=0
print(x)
for i in range(len(x)):
	result1= result1 * x[i]
print ('Product of digits is ' +str(result1)+ '.')

for i in range(len(x)):
	result2=result2 +x[i]
print('Sum of digits is ' +str(result2)+ '. ')

final= result1-result2
print ('Final answer is ' +str(final)+ '. ')
