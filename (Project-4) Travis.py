known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "Georgie", "Harry"]


while True:
    print("Hi! My name is Travis")
    validName=False
    while (not validName):
        name = input("What is your name?: ").strip().capitalize()
        if( name.isalpha()):
            validName=True
        else:
            print("""Error: Invalid Name! Please try again.""")
        

    if name in known_users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        
        if remove == "y":
            print(known_users)
            known_users.remove(name)
            print(known_users)
        elif remove == "n":
            print("No problem, I didn't want you to leave anyway!")

            
    else:
        print("Hmmm I don't think I have met you yet {}".format(name))
        validInput=False
        while (not validInput):
            add_me = input("Would you like to be added to the system (y/n)?: ").strip().lower()
            if (add_me=="y" or add_me=="n"):
                validInput=True
            else:
                print("""Error: Invalid Input! Please answer using "y" or "n". """)
        if add_me == "y":
            print(known_users)
            known_users.append(name)
            print(known_users)
        elif add_me == "n":
            print("No worries, see you around!")
    print("*"*30)
    #break
