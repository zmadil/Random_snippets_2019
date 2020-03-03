class Company:

	raise_salary=1.05   #Defining a class variable

	def __init__ (self,first,last,salary):
		self.first=first				#Instance variable, set using self argument
		self.last=last
		self.salary=salary
		self.email=first +'.'+last+'@Company.org'

	def fullname(self): #Method
		return self.first + ' '+ self.last

	def raise_salary(self):
		self.salary= int(self.salary * self.raise_salary)

employee1=Company('Zack','Hafoo',40000) #Instance of class
employee2=Company('Yonda','Balaji',2000)

print(employee1.salary)
employee1.raise_salary()
print(employee1.salary)
#print(employee1.fullname())
