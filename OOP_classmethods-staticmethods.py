import datetime  # need to import datetime to determine if it's a workday in the staticmethod below

class Employee:

	num_of_emps = 0
	raise_amt = 1.04
	
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_emps += 1


	def fullname(self):
		return f'{self.first}{self.last}'


	def apply_raise(self):
		self.pay = int(self.pay + self.raise_amt)

		#Classmethod
	@classmethod # Altering the funtion of a method to where we receive the Class as the first method rather than the instance or SELF
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount
	#Whats happening here is now when a raise_amt needs to be changed for the entire class
	#Ex: Employee.set_raise_amt(1.10) -- Now you've set the raise amount from 1.04 to 1.10 for the entire Employee class not just the instance of Employee
	# Can still call and run these from an instance of a class but it doesnt make sense to do so

	@classmethod
	def from_string(cls, emp_str): #When using Classmethod as an alternative consrictor you usually start the method with "from"
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay) # This line will create the new employee via the Class in this case Employee
		#Return is used here so when a string passes through the above class method, it will automatically return the given string without the - between
		#And automatically create a NEW instance of the Employee class
	# The above does the same thing as the example below commented out. instead of manually inputting each string to split
	# This class method will split strings automatically if they have '-'
	# Below is how you'd create the new instance of Employee with this classmethod

	#Defining Staticmethod to determine if its a workday for the employee
	@staticmethod         # This info is not something that can be pull from info from the Class Employee so we need to set a staticmethod 
	def is_workday(day):
		if day.weekday() == 5 or if day.weekday () ==6:
			return False
		return True
		#If you dont access the instance of the class anywhere in the method then it probably doesnt need to be a regular method and needs to be a staticmethod



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Tim', 'Ducharme', 65000)

#Turn a regular Method into a CLASSmethod
# use @ = Class decerator


#Example Below: You have a string of info for a new employee and you need to parse through the characters you dont need
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'
# To create a new Employee instance for each person with the given strings

#First you need to Split the string on the -
#first, last, pay = emp_str_1.split('-')

# Next - based on those values we could create a new Employee
#emp_3 = Employee(first, last, pay)

#OR you could use a CLASSMETHOD to do this...Example in the code block above

#The code below is the use of the Classmethod from_string to create new instances of employee with the emp_str
emp3 = Employee.from_string(emp_str_1)

print(emp3.email)

#Staticmethods - Dont pass the instance of the class. Include them in the classes because they have some logical connection to the class

#Say we wanted a simple function to take in a date and determine its a work day
#This doesnt depend on anything really from the Employee class so we need to create a Staticmethod. The example code is above