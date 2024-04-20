print("Welcome to Slot Machine Game!")

# get user input
def deposit():
    while True:
        amount = input('What would you like to deposit? $')
        if amount.isdigit(): # validation check
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else: 
            print("Please enter a number.")
    return amount
        