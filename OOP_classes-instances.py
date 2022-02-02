# Methods are class level functions
# Class Variables are variables that ALL instances of the class use
# Instance Variables are variables and values that are unique for each instance

class Employee:

	#When we DONT want to use SELF - for example if we wanted to have a running count of everytime a new employee was created
	num_of_emps = 0

	raise_amount = 1.04
	                                      # self is essentially taking about THIS current instance of a class. each instance of a class will be different
	def __init__(self, first, last, pay): #__init__ == initialize. takes "self" as first arguemnt as defualt -- sets the insance
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		#This __init__ method will run EVERYTIME we create a new Employee instance
		#Thats why we would put the num_of_emps counting code in this block
		#It will ONLY run once everytime a new employee is created!

		Employee.num_of_emps += 1
		# to add 1 everyime a new instance of Employee is created
		# adds 1 to a set Class variable num_of_emps


	#Method to generate this instance of an Employee class' full name
	def fullname(self): #we use self again because we want THIS INSTANCE of the Employee classes fullname
		return f'{self.first} {self.last}'


	# Method to apply a 1.04 raise to each employees pay. taking the pay for this instance of the class and multiplying
	# This method is a tougher if we needed to change the 1.04 if the rate changed we'd have to find this and change it manually. 
	# Or we can set a CLASS variable for this...code added above
	#def apply_raise(self):
	#	self.pay = int(self.pay * 1.04) 

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)



emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Tim', 'Ducharme', 65000)

#INSTANCE variable example -- emp_1.raise_amount = 1.10 -- this would set emp_1 to have a 1.10 raise amount
# While everyone else would have the raise_amount from teh Classes raise_amount value


#print(emp_2.__dict__) # Puts the employee into a dictionary 



#Lets say the company gives an anual raise of 1.04. we will set up a method in the Employee Class

#print(emp_1.email)
#print(emp_2.email)

#print(emp_2.fullname()) -- prints emp_2s full name using the fullname() function in the class

#To Call the method fullname()
# emp_1.fullname()
# Employee.fullname(emp_1) These both do the same thing

#To get employee full name here -- this is if the class doesnt have a method that generates this
# print(f'{emp_2.first} {emp_2.last}') in the example class above we created a method to this automatically