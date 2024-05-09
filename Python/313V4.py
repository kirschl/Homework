import math
total = 0
orderInformation=""

sandwich = input("Would you like a sandwich. (y/n) ")
if sandwich == "y":
    sandwich = input("Which sandwich would you like? chicken (c) $5.25, beef (b) $6.25, tofu (t) $5.75 ")
    if sandwich == "c":
        total +=  525 #add 5.25 to the total
        sandwich="chicken sandwich"
    elif sandwich == "b":
        total += 625
        sandwich="beef sandwich"
    elif sandwich == "t":
        total += 575
        sandwich="tofu sandwich"
    else:
        print("not on menu")
orderInformation+=f"Sandwich:\t{sandwich}\n"

drink = input("Would you like a beverage. (y/n) ")
if drink == "y":
    drink = input("Would you like a small $1.00 (s), medium $1.75 (m), or large $2.25 (l) ")
    if drink == "s":
        total+=1
    elif drink == "m":
        total+=175
    elif drink == "l":
        drink = input("Would you like a child sized for $0.38 more. (y/n) ")
        if drink == "y":
            drink = "c"
            total+=38 
        else:
            drink = "l"
        total+=225
orderInformation+=f"Drink:\t{drink}\n"

fries = input("Would you like fries. (y/n) ")
if fries == "y":
    fries = input("Would you like a small $1.00 (s), medium $1.75 (m), or large $2.25 (l) ")
    if fries == "s":
        total+=1
    elif fries == "m":
        total+=150
    elif fries == "l":
        fries = input("Would you like a mega sized for $0.50 more. (y/n) ")
        if fries == "y":
            fries = "m"
            total+=50 
        else:
            fries = "l"
        total+=200
orderInformation+=f"Fries:\t{fries}\n"

ketchup = input("Would you like ketchup. (y/n) ")
if ketchup == "y":
    ketchup=math.ceil(float(input("How many ketchups do you want. ($.10 each)")))
    total+=ketchup*10
orderInformation+=f"Ketchup:\t{ketchup}\n"

print(orderInformation)
print(f"Sub total: {total/100}")
print(f"total: {(math.ceil(float(total*.07+total)))/100}")
