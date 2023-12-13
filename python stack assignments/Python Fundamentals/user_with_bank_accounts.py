class BankAccount:
	
    def __init__(self, int_rate): 
        self.int_rate = int_rate
        self.interest = 0
        self.balance = 0
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    
    def deposit(self, amount):
        self.balance+= amount
        return self
	
    
    def yield_interest(self):
        if self.balance > 0:
            self.interest += self.balance * self.int_rate
            self.deposit(self.interest)
        else:
            self.balance -= 5.00



class User:

    def __init__(self, name, gender, city, state, interest_rate):
        self.name = name
        self.gender = gender
        self.city = city
        self.state = state
        self.myAccount = BankAccount(interest_rate)

    def user_deposit(self, amount):
        self.myAccount.deposit(amount)
        return self

    def user_withdrawal(self, amount):
        self.myAccount.withdraw(amount)

    def display(self):
        #return BankAccount.balance
        return f"My name is: {self.name}, and I have {self.myAccount.balance} in my account"

    



Brandon_Reed = User("Brandon", "Male", "Summerville", "SC", .003)
Brandon_Reed.user_deposit(5000).user_withdrawal(2000)


print(Brandon_Reed.display())
