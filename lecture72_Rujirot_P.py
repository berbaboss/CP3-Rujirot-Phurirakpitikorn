menulist = []
def showBill():
    print("-----My Food -----")
    for number in range(len(menulist)):
        print(menulist[number])
def Totalbill():
    y = 0
    for x in range(len(menulist)):
        y += menulist[x][1] #ใส่ [1] เพื่อเลือกตัวตำแหหน่งที่ 2 ใน list
    print("Total :",y)
while True:
    menuname = input("Please enter menu :")
    if(menuname.lower() == "exit"):
        break
    else:
        menuPrice = int(input("Price :"))
        menulist.append([menuname,menuPrice])
showBill()
Totalbill()

