balance = 50000.0
print("<<<<<<<<<<- ATM ->>>>>>>>>>>")
while True:
    print("1. Cheak balance..")
    print("2. Deposit money..")
    print("3. Withdraw money..")
    print("4. Exit..")

    choice = int(input("Ener your choice : "))

    if choice == 1:
        print(f"\nYour current balance is : {balance}\n")
    elif choice == 2:
        deposit = float(input(f"\nHow many amount you want to deposit : "))
        balance += deposit
        print(f"\nRs\= {deposit} deposited sucessfully.......\n")
    elif choice ==3:
        withdraw = float(input("\nHow many amount your want to withdraw : "))
        if balance >= withdraw:
            balance -= withdraw
            print(f"\nRs\= {withdraw} withdrew sucessfully......\n")
        else:
            print("\nInsufficient balance....\n")
    elif choice == 4:
        break



