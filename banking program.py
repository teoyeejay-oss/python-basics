#banking program

def balance():
    print(f"Your balance is RM{total:.2f}.")
    return total

def deposit():
    deposit_balance =  float(input("Please enter your deposit balance : "))
    if deposit_balance < 0 :
        print("Please enter a valid number")
        return 0
    else :
        return deposit_balance

def withdraw():
    withdraw_balance = float(input("Please enter your withdraw balance : "))
    if withdraw_balance > total :
        print("You haven't enough money,please enter a valid number.")
    return withdraw_balance




total = 0
while True:
    print("=============")
    print("1. balance")
    print("2. deposit")
    print("3. withdraw")
    print("4. quit ")
    print("================")
    choice = int(input("Please enter your choices : "))
    if choice == 1:
        balance()
    elif choice == 2 :
        total += deposit()
    elif choice == 3 :
        total = total - withdraw()
    elif choice == 4 :
        break
    else :
        print('Please enter a valid choice.')


