def login():
    usernameinput = input("Username : ")
    passwordinput = input("Password : ")
    if usernameinput == "admin" and passwordinput == "1234":
        showmenu()
    else:
        login()
def showmenu():
    print("----Bigberbshop----")
    print("1. Vat Calculator")
    print("2. Price Calculator")
    menuSelect()
def menuSelect():
    userSelected = int(input(">> "))
    if userSelected == 1:
        vatCalculate(int(input("Price :")))
    elif userSelected == 2:
        priceCalculate()
    else:
        menuSelect()
    return userSelected
def vatCalculate(totalprice):
    vat = 7
    result = totalprice + (totalprice * vat/100)
    print("Price :",result)
    return result
def priceCalculate():
    price1 = int(input("First Product Price : "))
    price2 = int(input("Second Product Price : "))
    return vatCalculate(price1+price2)

print(login())


