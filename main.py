print("Welcome to Slot Machine Game!")

MAX_LINES = 3

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

def get_lines():
    while True:
        lines = input('Enter the number of lines to bet on (1-' + str(MAX_LINES) + ")? ")
        if lines.isdigit(): # validation check
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else: 
            print("Please enter a number.")
    return lines

def main(): 
    balance = deposit()
    lines = get_lines()
    print(balance, lines)

main()