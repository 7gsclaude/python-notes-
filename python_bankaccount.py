import random

class BankAccount():
    def __init__(self, owner, balance, account_no):
        self.owner = owner
        self.balance = balance
        self.account_no = random.randint(111111111, 999999999)
    def deposit(self,amount):
        self.balance += amount
        return self.balance
    def withdrawl(self,amount):
        self.balance -= amount
        return self.balance


account1 = BankAccount("Claude", 1000, random)
account2 = BankAccount("kiko", 500, random )

# Make a deposit to account1
new_balance = account1.deposit(500)
print(f"Deposit of $500 made. New balance: ${new_balance}")

# Make a withdrawal from account2
new_balance = account2.withdrawl(200)
print(f"Withdrawal of $200 made. New balance: ${new_balance}")

# Print the attributes of the two instances
print(f"Account 1 owner: {account1.owner}, balance: ${account1.balance}, account number: {account1.account_no}")
print(f"Account 2 owner: {account2.owner}, balance: ${account2.balance}, account number: {account2.account_no}")
# This code creates two instances of the BankAccount class called account1 and account2, with the initial balance and owner name passed in as arguments. Then, it calls the deposit() and withdraw() methods on each instance and prints the balance after each transaction. Finally, it prints the attributes of each instance to check that they were created correctly.





