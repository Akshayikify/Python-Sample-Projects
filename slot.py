import random

TOTAL_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winings(columns,lines,bet,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings=values[symbol]*bet
            winning_lines.append(lines)
    return winnings,winning_lines

def get_machine_slot(rows,cols,symbols):
    all_symbols=[]
    for symbol,symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns=[]
    for col in range(cols):
        column=[]
        current_symb=all_symbols[:]
        for row in range(rows):
            value=random.choice(current_symb)
            current_symb.remove(value)
            column.append(value)
        columns.append(column) 
    return columns  

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!= len(columns)-1:
                print(column[row],end="|")
            else:
                print(column[row],end="")
        print()
             
def deposit():
    while True:
        amount=input("What would you like to deposit? ₹")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("The amount should be greater than 0.")
        else:
            print("Please enter the number.")
    return amount

def get_bet():
    while True:
        amount=input("What would you like to bet on each line ? ₹")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print(f"The amount should be between ₹{MIN_BET} and ₹{MAX_BET}")
        else:
            print("Please enter the number.")
    return amount

def get_num_lines():
    while True:
        lines=input(f"Enter the number of lines to bet on (1-{TOTAL_LINES}): ")
        if lines.isdigit():
            lines=int(lines)
            if lines>=1 and lines<=TOTAL_LINES:
                break
            else:
                print("Enter the valid number.")
        else:
            print("Please enter the number.")
    return lines

def spin(balance):
    lines=get_num_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f"You do not have enough to bet the amount. Your current balance is {balance}")
        else:
            break
 
    print(f"You're betting {bet} on {lines} lines. The total bet is: {total_bet}")
    slots=get_machine_slot(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    winnings,winning_lines=check_winings(slots,lines,bet,symbol_values)
    print(f"You won ₹{winnings}")
    print("You won on lines: ",*winning_lines)
    return winnings-total_bet
def main():
    balance=deposit()
    while True:
        print(f"The current balance is {balance}")
        answer=input('Press Enter to play (q tp quit) ')
        if answer=='q':
            break
        balance+=spin(balance)
    print(f"You left with {balance}")
main()