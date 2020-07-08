menulist = []
pricelist = []

def showBill():
    print("-----My Food -----")
    for number in range(len(menulist)):
        print(menulist[number],pricelist[number])

def Totalbill():
    y = 0
    for x in range(len(pricelist)):
        y += pricelist[x]
    print("Total :",y)

while True:
    menuname = input("Please enter menu :")
    if(menuname.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menulist.append(menuname)
        pricelist.append(menuPrice)
showBill()
Totalbill()


