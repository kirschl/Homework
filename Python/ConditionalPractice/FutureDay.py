days=["Sunday","Monday","Tuesday","Wensday","Thursday","Friday","Saturday"]
today = int(input("what is to day? (Sunday=0, monday=1,... saturday=6) "))
fDay = int(input("Enter number of days from to day "))

fDay=fDay+today
while fDay >= 7 :
    fDay= fDay-7

print(f"Today is {days[today]} and future date is {days[fDay]}")
