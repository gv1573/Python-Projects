import random #this library would be used for picking up random values for slot machine display

MAX_LINES=3
MAX_BET=100
MIN_BET=1


#we are now setting  up slot machine
rows=3  #number of rows in slot machine which will be displayed on each spin
cols=3  #number of columns in slot machine which will be displayed on each spin

#now we need to define the possible elements in each reel (column) of a slot machine, there are 3 reels and each reel can have multiple values
# Each reel can have multiple values but will only show random 3 values out of those total values

#setting up possible values in a machine (total 12 values per reel, 4 unique values, out of these 12, 3 would be displayed in each row)
symbol_count={  # we have created dict as same values have multiple occurance, so, we can place count as value of keys
    "A":3,
    "B":4,
    "C":2,
    "D":3
}

symbol_values={  # we have created dict as same values have multiple occurance, so, we can place count as value of key
    # this will check if let's say all three are A's, then winning=bet*value of A, so by betting 10 on line 1, if the person gets A, his winning as 30, if B, it is 40
    # the value of winnings is dependent on how frequent the value can come, so, if A is rare, its winning value would be high
    "A":3,
    "B":2,
    "C":4,
    "D":3
}

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]  # we have created this empty list to store possible values to be filled in a column/reel
    for symbol, symbol_count in symbols.items(): #itering through dict, symbols.items would give both keys and its values
        for _ in range(symbol_count):  # _ is used for anonymous variable, we can use it where we don't need a specific variable
            all_symbols.append(symbol) # storing all values from a dict to a list for easy accesibility

#now we need to add random values from all_symbols list to 3 rows and 3 columns of the slot machine
    columns=[]  #this will store values like columns[[a,b,c],[a,b,c],[a,b,c]]
    # we will have 3 columns to fill with values within 3 rows, we have created an empty column list and we will store 3-sub list in this column as 3 columns 
    for _ in range(cols):
        column=[]  #an empty sub-column of list which will be appended to columns list
        current_symbols=all_symbols[:]  #copying the symbols list to a new list as we need to remove values post eech iteration, ":" is used to create copy.
                                        #if we don't create copy, the original list would get impacted
        for _ in range(rows):  # total values to be generated in each column is equal to number of rows we fixed for slot machine
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)
    return columns


def print_slot_machine(columns): #calling slot machine function and printing the random list of values in each run
    for row in range(len(columns[0])):
        for i,column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")

        print()    



#defining the logic of winning game
def check_winnings(columns,lines,bet,values):
    winnings=0
    #winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings+=values[symbol]*bet
            #winning_lines.append(line+1)

    return winnings#,winning_lines
        
def deposit():
    while True:
        amount=input("What would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("amount should be greater than 0.")
        else:
            print("Please enter a number.")
    
    return amount

def get_number_of_lines():
    while True:
        lines=input("Enter number of lines to bet on (1-"+ str(MAX_LINES)+  ")?")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("enter a valid number of lines")
        else:
            print("Please enter a number.")
    
    return lines


def get_bet():
    while True:
        amount=input("What would you like to bet on each line?$")
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<=amount<=MAX_BET:
                break
            else:
                print("amount must be between $ ", str(MIN_BET), "and $", str(MAX_BET))
        else:
            print("Please enter a number")
    
    return amount


def spin(balance):
    lines=get_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print("You do not have enough balance. Your current balance is $",balance)
        else:
            break
    print("You are betting $",str(bet), "on", str(lines),"lines .Total bet is equal to: $",str(total_bet))

    slots=get_slot_machine_spin(rows,cols,symbol_count)
    print_slot_machine(slots)
    winnings=check_winnings(slots,lines,bet,symbol_values)
    print("You won $:",winnings)

    return winnings-total_bet


def main():
    balance=deposit()
    while True:
        print(f"Current balance is $ {balance}")
        answer=input("press enter to play (q to quit)")
        if answer=="q":
            break
        else:
            balance+=spin(balance)

        
    print(f"You left with ${balance}")

main()