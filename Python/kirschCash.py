change = float(input("Change owed: "))
coins =[0,0,0,0]

def cPrint(i):
    plural= ["Quarters","Dimes","Nickles","Pennies"]
    singular= ["Quarter","Dime","Nickle","Penny"]
    if coins[i]>1:
        print(f"{int(coins[i])} {plural[i]}")
    elif coins[i]==1:
        print(f"{int(coins[i])} {singular[i]}")

while change !=0:
    if change >= .25:
        coins[0]= change//.25
        change = round(change-((change//.25)*.25),2)
    elif change >= .10:
        coins[1]= change//.10
        change = round(change-((change//.10)*.10),2)
    elif change >= .05:
        coins[2]+= change//.05
        change = round(change-((change//.05)*.05),2)
    else:
        coins[3]= change//.01
        change = round(change-((change//.01)*.01),2)

for i in range(len(coins)):
    cPrint(i)

print(coins)

