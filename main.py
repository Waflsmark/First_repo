count = 0
bank_account = 687
max_tries = 3

while count < max_tries:    
    
    print(f"You have {max_tries - count} tries left")

    pin = input("Please enter your pin: ")

    if len(pin) == 4 or len(pin) == 6:
        if  pin == "4758" or pin == "475869":

            amount = int(input("How much money: "))
            if amount > 0 and amount < bank_account:
                print(f"Take your {amount} dollars")
                break

            else: 
                print("Error")

        else:
            print("Wrong pin")
    else:
        print("Error")

    count += 1

print("Good bye!") 