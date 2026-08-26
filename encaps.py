#encapsulation
class ATM:
    def __init__(self,balance):
        self.__balance = balance #private variable
    def deposit(self,amount):
        self.__balance += amount
        print("deposited:", amount)
    def withdrawl(self,amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print("withdrawl:", amount)
        else:
            print("insufficient balance")
    def check_balance(self):
        print("current balance:",self.__balance)
s = ATM(5000)
s.deposit(1000)
s.withdrawl(2000)
s.check_balance() 
