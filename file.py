# Bank system 

class Bank():
	def __init__(self, username, password, amount_money=0): # We strictly use 2 arguments which is username and password but the optional argument will be the amount of money
		self.username = username
		self.password = password
		self.amount_money = amount_money
		self.username_data = []
		self.password_data = []
		self.money = []
		
		
		

	def login(self):
		localname = ""
		localpassword = ""
		localmoney = 0

		# Check data in the database

		times = 0
		if self.username in self.username_data:
			if self.password in self.password_data:
				pass
		elif self.username not in self.username_data:
			if self.password not in self.password_data:
				while times < 5:
					if self.username in self.username_data and self.password in self.password_data:
						break
					times += 1
				print("Your username and password was not found in the database please register")
		
			

			

		
			


	def register(self):
		# To check if the username and the password that was passed is not already in the system
		if self.username in self.username_data and self.password in self.password_data:
			Bank.login()
		elif self.username not in self.username_data and self.password not in self.password_data:
			# Add their names to the system
			self.username_data.append(self.username)
			self.password_data.append(self.password)
			self.money.append(0)

			print("Register succesful")

	def withdraw(self):
		# Check for what account user wanted to withdraw the money
		if self.amount_money > 0:
			for i in range(len(self.username_data)):
				if self.username in self.username_data and self.password in self.password_data:
					if self.username == self.username_data[i] and self.password == self.password_data[i]:
						if self.money[i] > self.amount_money:
							self.money[i] -= self.amount_money
							print(f"Withdraw succest. You have {self.money[i]} left.")
							break
						elif self.money[i] < self.amount_money:
							self.money[i] = self.amount_money - self.money[i]
							print(f"Withdraw success. You have {self.money[i]} left")
							break
				else:
					output = f"""No account named {self.username} in the system.\n
					Please register first before withdrawing money from an account
					
					"""
					print(output, end=" ")

		else:
			raise "You don't have enough money to withdra"

	def deposit(self):
		if self.amount_money != 0:
			for i in range(len(self.username_data)):
				if self.username in self.username_data and self.password in self.password_data:
					if self.username == self.username_data[i] and self.password == self.password_data[i]:
						self.money[i] += self.amount_money
						print("Deposit success")
						break
			 	 
			
		else:
			output = """ Please enter the money in the argument of the class
			
			"""
			print(output)

# Create an object for class Bank

username_input = input("Please enter your username : ")
password_input = input("Please enter your password : ")
confirm = input(str("Do you want to withdraw or not (Enter only true or false) : "))
amount_money_input = 0

if confirm == "True" or confirm == "true":
	money = input("Please enter the amount of money that you wanted to withdraw or deposit : ")
	amount_money_input += int(money)
elif confirm == "False" or confirm == "false":
	pass
	
# Class object

b = Bank(username_input, password_input, 45454)

b.register()
print(b.username_data)
print(b.password_data)
print(b.money)
b.deposit()
print(b.money)
