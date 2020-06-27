usernameInput = input("Username : ")
passwordInput = input("Password : ")
if usernameInput == "admin" and passwordInput == "password":
    print("Hello Welcome !")
    print("----- Product -----")
    print("1.Shirt   250 THB")
    print("2.T-Shirt 150 THB")
    print("3.Pants   200 THB")
    print("4.Jean    350 THB")
    print("5.Jacket  500 THB")
    userSelected = int(input("Choose product Number : "))
    if userSelected == 1:
        amount1 = int(input("Amount of Shirt : "))
        print("Total cost =",250 * amount1+(250*amount1*7/100))
    elif userSelected == 2:
        amount2 = int(input("Amount of T-Shirt: "))
        print("Total cost =",150 * amount2+(150*amount2*7/100))
    elif userSelected == 3:
        amount3 = int(input("Amount of Pants: "))
        print("Total cost =",200 * amount3+(200*amount3*7/100))
    elif userSelected == 4:
        amount4 = int(input("Amount of Jean: "))
        print("Total cost =",350 * amount4+(350*amount4*7/100))
    elif userSelected == 5:
        amount8 = int(input("Amount of Jacket: "))
        print("Total cost =",500 * amount5+(500*amount5*7/100))
else:
    print("Incorrect Username or Password")