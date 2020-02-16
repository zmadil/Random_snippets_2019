class Employee:

	raise_amount= 1.05
	num_emps=0

	def __init__ (self,fname,lname,pay): #method always take instance which is self.
		self.fname=fname 				#instance variable
		self.lname=lname
		self.pay=pay
		self.email= fname+'.'+lname + '@gmail.com'
		Employee.num_emps+=1	#init method always run when instance is created

	def fullname(self):
		return ('{} {}'.format(self.fname, self.lname))


	def pay_raise(self):
		self.pay= int(self.pay * self.raise_amount)

#employee1 and 2 are instances. Thats why method always take self argument
employee1=Employee('Zain','Adil', 4000)
employee2= Employee ('Adil', 'Zain', 5000)

# print (employee1.fullname())
# print (employee2.fullname())
# print (employee1.pay)
# employee1.pay_raise()
# print (employee1.pay)

#if you change employee class variable amount, every instance changes. Not true if you change instance variable!

print(employee1.raise_amount)
print (Employee.raise_amount)
print (Employee.num_emps)