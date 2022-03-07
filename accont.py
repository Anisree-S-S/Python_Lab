class Bankaccount:
    def __init__(self):
        self.accno=int(input("enter the account number : "))
        self.name=input("enter the account holder name : ")
        self.acctype=input("enter the account type : ")
        self.balance=0
    def deposit(self):
        print('')
        amount=int(input("enter the amount to deposit  : "))
        self.balance+=amount
        print(amount," successfully deposited ")
    def withdrawn(self):
        print('')
        amount=int(input("enter the amount to withdrawn "))
        if amount>self.balance:
            print("insufficient balance!!!!!")
        else:
            self.balance-=amount
            print(amount," is withdrawn ")
            print("the current balance is ",self.balance)
    def display(self):
        print('')
        print("Account Details........")
        print("Account number : ",self.accno)
        print("Name of account holder : ",self.name)
        print("Account type : ",self.acctype)
        print("Available balance : ",self.balance)
obj=Bankaccount()
obj.deposit()
obj.withdrawn()
obj.display()