import random

capLetters= int(input("How many capital letters: "))
lowLetters= int(input("How many lower case letters: "))
num= int(input("How many numbers: "))
specialChar= int(input("How many special characters: "))
password=""

for i in range(capLetters):
    password+= chr(random.randint(ord('A'), ord('Z')))

for i in range(lowLetters):
    password+= chr(random.randint(ord('a'), ord('z')))

for i in range(num):
    password+= f"{random.randint(1,9)}"

for i in range(capLetters):
    password+= chr(random.randint(ord('!'), ord(')')))

password = list(password)
random.shuffle(password)
print (''.join(password))

#geeksforever helped do random letters
#stack overflow for shuffle
