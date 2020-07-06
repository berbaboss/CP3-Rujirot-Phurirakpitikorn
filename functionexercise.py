def vatCalculate(totalprice):
    return totalprice+(totalprice*7/100)
price = int(input("Price : "))
print("Total price include vat",vatCalculate(price))

