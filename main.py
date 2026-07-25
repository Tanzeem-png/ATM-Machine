def line():
    print("=" * 40)
def intro():
    line()
    print("TANZEEM'S BANK")
    line()

balance = 0

def check_balance():
    line()
    print("Bank Statement")
    line()
    global balance
    print()
    print("You Currently Have : ",balance,"$")
    print()
    




def add_money():
    line()
    print("Deposit")
    line()
    global balance
    print()
    ask = int(input("How Much Money Wanna Deposit : " ))
    print()
    balance += ask

def spend_money():
    line()
    print("Withdraw")
    line()
    global balance
    print()
    ask2 = int(input("How Much Money Wanna Withdraw : " ))
    print()
    if balance < ask2:
        print()
        print("Insuffcient Balance")
        print()
        print("You Have",balance,"$ In Your Account")
        print()
        spend_money()
    else:
        balance -= ask2
        

def choose_section():
    print()
    print()
    print("1 . Check Balance ")
    print()
    print("2 . Deposit Balance ")
    print()
    print("3 . Withdraw Balance ")
    print()
    print("4 . Exit ")
    print()


def main():
    intro()
    choose_section()
   
    choice = int(input("Choose An Action : " ))
    if choice == 1:
        check_balance()
        print()
        print()
        ask = input("You Wanna Go Back? (y) : ")
        if ask == "y":
            print()
            main()
    

    elif choice == 2:
        print()
        add_money()
        print()
        print()
        main()
        

    elif choice == 3:
        print()
        spend_money()
        print()
        print()
        main()
        
    elif choice == 4:
        print()
        print()
        print("Thanks For Using My Programme ")
        print()
    else:
        print()
        print("Invalid Request")
        print()
        main()





main()

    

