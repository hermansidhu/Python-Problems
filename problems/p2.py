# ARS Gems Store sells different varieties of gems to its customers. Write a Python
# program to calculate the bill amount to be paid by a customer based on the list of
# gems and quantity purchased. Any purchase with a total bill amount above Rs.30000
# is entitled for 5% discount. If any gem required by the customer is not available in the
# store, then consider total bill amount to be -1. Assume that quantity required by the
# customer for any gem will always be greater than 0. Perform case-sensitive
# comparison wherever applicable.


def calculate_bill_amount(gem_prices, reqd_gem_quantities):

    gem_prices = dict((k.lower(), v) for k, v in gem_prices.items())
    reqd_gem_quantities = dict((k.lower(), v)
                               for k, v in reqd_gem_quantities.items())

    bill_amount = 0
    for gem in reqd_gem_quantities:
        if gem in gem_prices:
            price = gem_prices[gem] * reqd_gem_quantities[gem]
            bill_amount += price
        else:
            return -1
    if bill_amount > 30000:
        return bill_amount-(bill_amount*0.05)
    else:
        return bill_amount


# available gems and their prices in a dictionary
gem_prices = {"Red": 2000, "Green": 3000,
              "Blue": 4000, "Yellow": 4000, "Purple": 60000}

print()
print("Color: Price")
print(gem_prices)


# creating a new dictionary for the required gems using a for loop
n = int(input("How many colors you want to buy : "))
reqd_gem_quantities = {}
for i in range(n):
    key = input("Enter color : ")
    value = int(input("Enter quantity : "))
    reqd_gem_quantities[key] = value
print(reqd_gem_quantities)

print(calculate_bill_amount(gem_prices, reqd_gem_quantities))
print()
