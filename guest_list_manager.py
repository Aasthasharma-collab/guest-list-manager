print("AA exclusive club".upper())
guest_list = {"karan aujla", "honey singh", "vedant", "nidhi"}
vip_list = {"me", "ronaldo", "mia", "blush"}
already_inside=set()

while True:
    print('Welcome to the party')

    print('Help me with your name')
    name = input(" ").strip().lower()
    if not name:
        print("No name entered. Exiting.")
        import sys
        sys.exit()

    age=int(input("may i know your age: "))
    if age<21:
        print("sorry, your age must be 21 or above to enter")
        continue
    
    print("Let me check")
    
    if name in already_inside:
        print(f"w8,someone named {name.title()} is already inside")    
        different_person=input("are you diff person with same name?(yes/no): ").strip().lower()
        if different_person!="yes":
            print("access denied! duplicate entry detected")
            continue
        else:
            print("since you are diff person, you must buy a ticket")
            buy_ticket = input("would you like to party ;)?(yes/no): ").strip().lower()
            if buy_ticket == "yes":
                try:
                    count = int(input("how many tickets you would like to buy: "))
                except ValueError:
                    print("Invalid number of tickets.")
                    continue
                grand_total = count * 100
                print(f"your total would be {grand_total}")
                print("welcome to the party!")
                already_inside.add(name)
                continue
            else:
                print("okay, thank you")
                continue                                                                                 
    elif name in vip_list:
        print(f"Welcome {name.title()}")
        print("Your entry will be from the golden gate")
        print("enjoy your night :)")

        already_inside.add(name)
    elif name in guest_list:
        print(f"Welcome {name.title()}")
        print("your entry will be from this side")
        already_inside.add(name)
     
    else:
        print("Sorry, I don't see your name on the list")
        new_person = input("Do you want to buy a ticket? (yes/no): ").strip().lower()
        if new_person == "yes":
            try:
                count=int(input("how many tickets: "))
            except ValueError:
                print("ivalid no. of tickets")
                continue
            grand_total=count*100
            print(f"your total is{grand_total}")
            print(f"Welcome {name.title()} :)")
            already_inside.add(name)
        else:
            print("Okay, thank you")
