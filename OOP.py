class Company:
	def __init__ (self,first,last,salary):
		self.first=first
		self.last=last
		self.salary=salary
		self.email=first +'.'+last+'@Company.org'

	def fullname(self): #Method
		return self.first + ' '+ self.last

employee1=Company('Zack','Hafoo',40000) #Instance of class
employee2=Company('Yonda','Balaji',2000)

#print(employee1.fullname())
#print(employee1.fullname())