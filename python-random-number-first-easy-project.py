import random

print("Hello player")
print("Program generate number from 1 to 100. You job is try to guess what number is generated")
print("Remember. From you belong decision how hard version you want. You have between 1 to 10 try")
print("Good luck")

numberOfTry=0

while True:
    numberOfTry = int(input("how many try you want? "))
    if numberOfTry < 1 or numberOfTry > 10:
        print("You have bad number of try, number have been between 1 - 10")
        continue
    else:
        break
difficulty = ""

if numberOfTry < 4:
    difficulty="hard"
elif numberOfTry < 7:
    difficulty="medium"
else:
    difficulty="it's easy you pussy"
    
print("you choice ", difficulty, "level")        

randomNumber = random.randint(1,100)
print(randomNumber)
userNumber = 0
count = 0
count2 = numberOfTry
while count < numberOfTry :
    
    print("now, you have ", count2, "try")
    count2 -=1
    userNumber = int(input("Give me you number"))
    count += 1
    if randomNumber == userNumber:
        print("good work, you guess number with", count, "time's on", difficulty, "level")
        break
    elif randomNumber != userNumber:
        if randomNumber > userNumber:
            print("You number is to small")
        else:
            print("You number is to big")
if count == numberOfTry:
    print("Sorry, you lose")
input("\n\nPress Enter to end program")