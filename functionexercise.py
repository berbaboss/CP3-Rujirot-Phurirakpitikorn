def vatCalculate(totalprice):
    result = totalprice+(totalprice*7/100)
    return result
price = int(input("Price : "))
print("Total price include vat",vatCalculate(price))

