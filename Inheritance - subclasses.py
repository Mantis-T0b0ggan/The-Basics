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




#creating developer subclass
class Developer(Employee): 
# The argument being passed here is the Employee CLASS. This is whats being inherited 
	raise_amt = 1.10 # This would be changing the raise amount for any Developer subclass to 1.10 from 1.04 in the 
	#regular Employee Class instances 
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first, last, pay) 
		# This allows the Inherited class (Emlpoyee here) to pass the first, last, pay values as we only to Developer to add prog_lang
		self.prog_lang = prog_lang

"""Say we wanted to add a Programming Language section for Developers only. While other employees hsve first, last, pay. 
The Developer subclass will have first, last, pay, programming language. To do this the example is above"""

#Here we are going to create the Manager SUBCLASS
#Manager subclass will have a list of employee's they manage
#setting emlpoyees to None to initiate an empty list. never want to pass mutabe data types as arguments
class Manager(Employee): 
	def __init__(self, first, last, pay, employees=None): 
		super().__init__(first, last, pay) 
		if employees is None: 
		#if the employee list == None a new empty list is created called employees
			self.employees = []
		else:
			self.employees = employees  
			#If the list exists, then the instance adds to the employee list

#adding a function to add an employee from the managers list 
	def add_emp(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)
# this checks to see if the employee is already in the employee list created above. If they are not the given emp in the argument
# is appended to the employees list

#adding a function to remove employee
	def remove_emp(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)
# this checks to see if the employee is already in the employee list created above. If they are, the emp name given in the argument
# is removed to the employees list


#to print out the list of employees the manager supervises
	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())
	# This method prints out the emps full name and iterates through the emploees list


dev1 = Developer('Corey', 'Schafer', 50000, 'Java')
dev2 = Developer('Tim', 'Ducharme', 65000, 'Python')
mgr1 = Manager('Sue', 'Smith', 90000, [dev1])

#print(mgr1.email)
#mgr1.print_emps()

#mgr1.add_emp(dev2)
#mgr1.print_emps()

#mgr1.remove_emp(dev1)
#mgr1.print_emps()


#Inheritance allows us to inherit attributes and methods from a parent class
# useful because we can create new subclasses with parts of multiple classes

"""Give the code we've used on the other examples, lets say the company wants
to create different employees such as devs and managers. We'd need to create a subclass for this because both devs and managers are going to have
a first, last, email and pay just like everyone else. But they will have their own attributes they dont share."""

# print(help(Developer)) -- This shows you whats going on when this class is called. This helps understand how the computer traced around to find 
# the info it needs. In this case it would look for the __init__ which lives in the Employee class. 

# isistance() will tell us if a given argument is an instance of a class or not. Example print(mgr1, Manager))
# This would print True - as its an instance of the Manager class. If you checked if mgr1, Developer - it'd return False
# Because they are not of the same subclass

#issubclass lets us know if a given argument is a subclass. Example issubclass(Developer, Employee) == True
#issubclass(Manager, Employee) == True  issubclass(Manager, Developer) == False. Manager is not a subclass of Developer

