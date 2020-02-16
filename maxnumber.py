number= 6969

lista=list(map(int,str(number)))
print(lista)

for i in range(len(lista)):
	if lista[i]==6:
		lista[i]=9
		break

print (lista)
print('--------------')
print('largest value is ')
for i in range(len(lista)):
	print (lista[i], end=' ')

