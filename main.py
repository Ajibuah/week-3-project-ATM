# ATM PROCESS
# Assume your card is in the machine
try:
    with open("user_pin.txt", "r") as pin_file:
        user_pin = int(pin_file.read())
except FileNotFoundError:
    user_pin = None
if user_pin is None:
    user_pin = int(input("Please set your PIN: "))
    with open("user_pin.txt", "w") as pin_file:
        pin_file.write(str(user_pin))
    print("Your PIN is set.")
try:
    with open("user_balance.txt", "r") as balance_file:
        user_balance = float(balance_file.read())
except FileNotFoundError:
    user_balance = 1000.0
    with open("user_balance.txt", "w") as balance_file:
        balance_file.write(str(user_balance))
while True:
    print(f"Your account balance: N{user_balance: 2}")
    choice = int(input("""Select your ATM transaction:
    1. Withdraw
    2. Transfer
    3. Buy Airtime
    4. Change Pin
    5. Quit
    Enter the number corresponding to your choice: """))

    if choice == 1:
        pin = int(input("Please enter your PIN: "))
        if pin == user_pin:
            withdrawal_amount = float(input("Please enter the amount to withdraw: "))
            if withdrawal_amount <= user_balance:
                user_balance -= withdrawal_amount
                with open("user_balance.txt", "w") as balance_file:
                    balance_file.write(str(user_balance))
                print(f"Withdrawal Successful. Your new balance is ${user_balance:.2f}")
            else:
                print("Insufficient funds. Withdrawal failed.")
        else:
            print("Invalid PIN. Withdrawal failed.")
    elif choice == 2:
        pin = int(input("Please enter your PIN: "))
        if pin == user_pin:
            transfer_amount = float(input("Enter the amount to transfer: "))
            receiver_account_number = input("Enter receiver's account number: ")
            receiver_account_name = input("Enter receiver's account name: ")
            if transfer_amount <= user_balance:
                user_balance -= transfer_amount
                with open("user_balance.txt", "w") as balance_file:
                    balance_file.write(str(user_balance))
                print(f"Transfer Successful. Your new balance is ${user_balance:.2f}")
            else:
                print("Insufficient funds. Transfer failed.")
        else:
            print("Invalid PIN. Transfer failed.")
    elif choice == 3:
        pin = int(input("Please enter your PIN: "))
        if pin == user_pin:
            airtime_amount = float(input("Please enter the amount for airtime purchase: "))
            if airtime_amount <= user_balance:
                user_balance -= airtime_amount
                with open("user_balance.txt", "w") as balance_file:
                    balance_file.write(str(user_balance))
                print(f"Buy Airtime Successful. Your new balance is ${user_balance:.2f}")
            else:
                print("Insufficient funds. Buy Airtime failed.")
        else:
            print("Invalid PIN. Buy Airtime failed.")
    elif choice == 4:
        old_pin = int(input("Enter your old PIN: "))
        if old_pin == user_pin:
            new_pin = int(input("Enter your new PIN: "))
            user_pin = new_pin  # Update the user's PIN with the new PIN
            with open("user_pin.txt", "w") as pin_file:
                pin_file.write(str(new_pin))
            print("Change Pin Successful")
        else:
            print("Invalid old PIN. Change Pin failed.")
    elif choice == 5:
        print("Thank you for using the ATM. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid transaction.")
