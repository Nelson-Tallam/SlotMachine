import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3 

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(cols, rows, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
            
            
    columns = []
    for col in range(cols):
        columns = []
        for row in range(rows):
            value = 
    
def deposit():
    while True:
        amount = input("What amount would you like to deposit?Ksh.")
        if amount.isdigit():
            amount= int(amount)
            if amount>0:
                break
            else:
                print("Amount must be more than 0.")
        else:
            print("Please enter a number")
    return amount


def get_number_of_lines():

    while True:
        lines = input("Enter the number of lines to bet on(1-"+ str(MAX_LINES)+")?")
        if lines.isdigit():
            lines= int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    return lines

def get_bet():
    while True:
            amount = input("What amount would you like to bet on each line?Ksh.")
            if amount.isdigit():
                    amount= int(amount)
                    if MIN_BET<= amount<= MAX_BET:
                        break
                    else:
                        print(f"Amount must be between Ksh{MIN_BET}- Ksh{MAX_BET}.")
            else:
                    print("Please enter a number")
    return amount

def main():
    balance = deposit()
    lines = get_number_of_lines()
    while True:
        
        bet = get_bet() 
        total_bet = bet * lines
        
        if total_bet > balance:
            print(f"You do not have enough funds to bet that amount. Your balance is: {balance}")
        else:
            break    
        
    print (f"You are betting Ksh. {bet} on {lines} lines. Your total bet amount is: Ksh.{total_bet}")

main()

