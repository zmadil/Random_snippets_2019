list1= [1,2,3,4,5,6,7,8]

evens=list(filter(lambda n:n%2==0,list1))  #filter filters it, cant change the value. With maps you can change the values.
print(evens)


double_it= list(map(lambda n: n*2,evens))  #Can alter the value
print(double_it)
