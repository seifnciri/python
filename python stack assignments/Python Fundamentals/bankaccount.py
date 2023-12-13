class BankAccount:
	
    def __init__(self, int_rate, name, gender, city, state): 
        self.name = name
        self.gender = gender
        self.city = city
        self.state = state 
        self.int_rate = int_rate
        self.interest = 0
        self.balance = 0
    
    def withdraw(self, amount):
        self.balance -= amount
        return self
    
    
    def deposit(self, amount):
        self.balance+= amount
        return self
	


    def display_account_info(self):
        #return f'My interest rate is {self.int_rate} My name is: {self.name} I am a: {self.gender} I was born in: {self.city}, {self.state}'
        print("my interest rate is", self.int_rate, "My name is:", self.name, "I am a:", self.gender, "I was born in:", self.city, self.state)
    def yield_interest(self):
        if self.balance > 0:
            self.interest += self.balance * self.int_rate
            self.deposit(self.interest)
        else:
            self.balance -= 5.00




Noah = BankAccount(.199,"Noah", "male", "Summerville", "South Carolina" )
Brandon= BankAccount(.299,"Brandon", "male", "Honolulu", "Hawaii")

Noah.display_account_info()
Noah.deposit(10000).withdraw(5000).withdraw(4000).yield_interest()
print(Noah.balance)
Brandon.display_account_info()
Brandon.deposit(100).withdraw(500).yield_interest()
print(Brandon.balance)




