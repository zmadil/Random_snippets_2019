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

	@classmethod
	def set_amount (cls, rakam):
		cls.raise_amount=rakam

	@classmethod
	def from_str (cls, string):
		first,last,pay= string.split('-')
		return cls(first,last,pay)

	@staticmethod
	def is_workday (day):
		if day.weekday ==5 or day.weekday == 6:
			return False
		return True 

import datetime
myday= datetime.date(2019,12,10)

print (Employee.is_workday(myday))

employee5='Zain-Adil-1000'
newemployee5= Employee.from_str(employee5)
#employee1 and 2 are instances. Thats why method always take self argument
employee1=Employee('Zain','Adil', 4000)
employee2= Employee ('Adil', 'Zain', 5000)

print (newemployee5.pay)

# print (employee1.fullname())
# print (employee2.fullname())
# print (employee1.pay)
# employee1.pay_raise()
# print (employee1.pay)

#if you change employee class variable amount, every instance changes. Not true if you change instance variable!
Employee.set_amount(1.1)

print(employee1.raise_amount)
print (Employee.raise_amount)
print (Employee.num_emps)