# from sys import exit

balance = 0.0

def deposit(balance, amount): 
  amount = float(input("Summani kiritin")) 
  balance += amount

def withdraw(balance, amount):
    amount = float(input("Yechiladigan summa"))         #Foydalanuvchining balansi bor. U `deposit`, `withdraw` yoki `check balance` qiladi.
    if amount <= balance:
            balance = amount
    else:
        print("Balans yetarli emas ")

def check_balance(balance):
    print("Balans",balance)
    

while True:
    print("1. Deposit \n2. Withdraw \n3. check_balance \n4. exit")

    choice = input("Tanlang; ")
    
    if choice == 1:
        deposit()
    elif choice == 2:
        withdraw()
    elif choice == 3:
        check_balance()
    elif choice == 4:
        break
    else:
        print("Notug'ri tanlov")
