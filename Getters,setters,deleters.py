class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		#self.email = first + '.' + last + '@company.com'

	@property            #adding @Property allows us to acces the method as a property so it wouldnt affect current code
	def email(self):
		return f'{self.first} {self.last}@company.com'
#Without the property decerator the code will work but in order to be called now it would need to look like print(self.email())
#This would break the code for current employees and you'd have to individually change the code. OR you can use the property decerator
	def fullname(self):
		return f'{self.first} {self.last}'

#Using Setters: use the @ and the method you want to use as the setter. in this case the fullname function
	@fullname.setter
	def fullname(self, name) #In this case here name is the value we're trying to set
		first, last = name.split(' ')
	#This will split a given name in 2 parts. the first part before the space is first, the other part after the space is last
	#This sets the first name and last name of the employee

	#to make a DELETER - only accepts self value
	@fullname.deleter
	def fullname(self):
		print('Delete Name!')
		self.first = None
		self.last = None
#This code would be run anytime we delete an attributes in an employee
#example del emp1.fullname -- this sets emp1 first and last attributes to None


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Tim', 'Ducharme', 65000)

"""In this example, if we wanted to change the first or last name of an employee we could easily do so
however when creating the e-mail it will not get the new value from the updated first or last name. 
If someone got married and changed their last name the company wants to be able to change the users
last name and have it reflect on the e-mail address as well. Example code above in the block

We would need to use a property dececator - allows us to define a method but access it like an attribute.

