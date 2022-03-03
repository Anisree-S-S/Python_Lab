class Bank:
    accountNo = ""
    name = ""
    typeOfAccount = ""
    balance = 0

    def __init__(a,accountNo,name,typeOfAccount,balance):
       a.accountNo = accountNo
       a.name = name
       a.typeOfAccount = typeOfAccount
       a.balance = balance

    def deposit(a,amount):
       a.balance = a.balance + amount
       print("\nAmount {} is credited on your account {}\n Avaialable balance: {}".format(amount,a.accountNo,a.balance))

    def withdraw(a,amount):
       if(amount>a.balance):
          print("Insufficient Balance \n Available Balance:",a.balance)
       else:
        a.balance = a.balance - amount
        print("\nAmount {} is debited from your account {}\n Avaialable balance: {}".format(amount,a.accountNo,a.balance))


accno=input("Enter your accound number: ")
accname=input("Enter account holder name: ")
acctype=input("Choose your account type \n a.Savings b.Current c.Fixed \n")
accbal=int(input("Enter current bank balance: "))

acc = Bank(accno,accname,acctype,accbal)
choice=input("Select your option \n a. Withdrawal \n b. Deposit \n Type a/b :")
if(choice=='a'):
   amt=int(input("Enter the amount: "))
   acc.withdraw(amt)
elif(choice=='b'):
   amt=int(input("Enter the amount: "))
   acc.deposit(amt)
else:
   print("Please enter a valid option a/b")