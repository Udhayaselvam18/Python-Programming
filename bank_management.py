balance = 0

while True:
    print("\n--- BANK MANAGEMENT SYSTEM ---")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("Current Balance:", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: "))

        if amount > 0:
            balance += amount
            print("Amount Deposited Successfully!")
        else:
            print("Enter a valid amount")

    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount > 0 and amount <= balance:
            balance -= amount
            print("Withdrawal Successful!")
        else:
            print("Insufficient Balance or Invalid Amount")

    elif choice == "4":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")
