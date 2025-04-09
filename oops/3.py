class BankAccount:

    def __init__(self, account_holder, balance=0):

        self.account_holder = account_holder  # Public
        
        self.__balance = balance              # Private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ₹{amount}. Remaining balance: ₹{self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def check_balance(self):
        return f"Account Balance: ₹{self.__balance}"

# Creating an object
acc = BankAccount("Rahul", 5000)

# Accessing methods (public interface)
acc.deposit(2000)       # ✅ allowed
acc.withdraw(1000)      # ✅ allowed
print(acc.check_balance())

# Trying to access private attribute directly
print(acc.__balance)    # ❌ AttributeError

# But can be accessed (not recommended) using name mangling
print(acc._BankAccount__balance)  # ⚠️ not recommended
