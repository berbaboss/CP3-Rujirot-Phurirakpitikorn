number = int(input("Please type :"))
for i in range(number):
    text = ""
    space = " "
    text = text + (2*i+1)*"*"
    space = space*(number-1)
    number -= 1
    print(space+text)

