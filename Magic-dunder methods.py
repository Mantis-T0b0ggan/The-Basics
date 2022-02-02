class Employee:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

	def fullname(self):
		return f'{self.first} {self.last}'

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

#
	def __repr__(self):
		return f"{self.first} {self.last} {self.pay}"
	#Trying to return a string to re-create the object being called

	def __str__(self):
		return f'{self.fullname()} - {self.email}'
	#Creating a return so when the employee is printed it returns to the end-user in a very easy to read way


	#If we wanted to add all the salaries of all employees together easily we could use the __add__ special method
	def __add__(self, other):
		return self.pay + other.pay


	#If you want the len() method to work on your object you'd need to use the __len__ special method
	def __len__():
		return len(self.fullname())
		#This would return the amount of characters in a given instance of an employees full name


emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Tim', 'Ducharme', 65000)

print(emp1 + emp2)

"""If you ever need to find out what a function does you can always go to the library online and it'll show you what the arguments
it takes as well as what it does.

Special or Magic Methods - allow us to emulate some built-in behavior in python but also implement operator overloading
example if we add to strings together print('a' + 'b') would bring out 'ab' but print(1 + 2) would print 3 obviously
If we were to try to do print(dev1) you'd get a non descriptive return. We would use these Special Methods to make this return
something more valuable to us. 
Special Methods are ALWAYS surrounded by double underscores __SpecialMethod__ -- often called dunders
__init__ is a special method. 
-- repr(emp1) -- should be used for debugging and logging - meant to seen by developers
Need to AT LEAST have an repr method. If we have repr, then when calling str on an employee it will display the repr as a fallback
RULE OF THUMB when creating repr methods - try to display something that you can copy and paste back into python code to re-create that object
AFTER you've created your repr method, now when calling to print the employee the return will use this repr method and display a re-created version
of that employee to display. 



-- str(emp1) -- more of a readable representation of the object. Intended to be seen by the end-user"""








#Below is code from the Inheritance file
"""class Developer(Employee): 
	raise_amt = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) 

		self.prog_lang = prog_lang



class Manager(Employee): 
	def __init__(self, first, last, pay, employees=None): 
		super().__init__(first, last, pay) 
		if employees is None: 
			self.employees = []
		else:
			self.employees = employees  

	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())"""
