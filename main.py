import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
ROWS = 3
COLS = 3

# Set up slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check: # break if line symbols dont match
                break
        else: 
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines
        

def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    # add the symbols into the list based on count
    for symbol, symbol_count in symbols.items(): #loop for key & value
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = [] # [[], [], []]
    for _ in range(cols): # loop through col
        column = []
        # make a copy of all_symbols list
        current_symbols = all_symbols[:]
        for _ in range(rows): # loop through row
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
    
def print_slot_machine(columns):
    # [A, B, C]
    # [B, A, A]
    # [C, B, C]
    # matrix transposing
    for row in range(len(columns[0])):
        for i, column in enumerate(columns): # get index + value with enumerate
            if i != len(columns) - 1:
                print(column[row], end=" | ") # end default to \n next line
            else: 
                print(column[row], end="")
        print() # empty print to go to new line

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

def get_bet():
    while True:
        amount = input('What would you like to bet on each line? $')
        if amount.isdigit(): # validation check
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} ${MAX_BET}.")
        else: 
            print("Please enter a number.")
    return amount

def spin():
    lines = get_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount, your current balance is: ${balance}")
        else: 
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines) # pass ref to winning_lines
    return winning_lines - total_bet

def main(): 
    print("Welcome to Slot Machine Game!")
    balance = deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin()
    print(f"You left with ${balance}")

main()