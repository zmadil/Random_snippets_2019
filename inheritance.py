class Employee:

	raise_amount= 1.09
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

class Dev(Employee): 
	raise_amount=1.10  #overwrites the original class raiseamount value
	def __init__ (self,fname,lname,pay,prog_lang):
		super().__init__(fname,lname,pay) # so it inherits this from parent class
		self.prog_lang= prog_lang



dev1= Dev('Muhammad','Adil', 2000,'Python')
print(dev1.prog_lang)
dev1.pay_raise()
print(dev1.pay)




