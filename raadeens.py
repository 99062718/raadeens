import random

x = 1
randomNum = 0
score = 0
aantalGeraden = 0

while x < 21:
    y = 0
    randomNum = random.randint(1, 1000)
    print("ronde", x)
    while y < 10:
        antwoord = int(input("voer een getal in tussen 1 en 1000: "))
        if antwoord == randomNum:
            y = 10
            score += 1
            print("U heeft het antwoord geraden!")
        elif antwoord - randomNum <= 20 and antwoord - randomNum > 0 or randomNum - antwoord <= 20 and randomNum - antwoord > 0:
            print("U bent heel warm")
        elif antwoord - randomNum <= 50 and antwoord - randomNum > 0 or randomNum - antwoord <= 50 and randomNum - antwoord > 0:
            print("U bent warm")
        elif antwoord > randomNum:
            print("U moet lager raden")
        else:
            print("U moet hoger raden")
        y += 1
        aantalGeraden += 1
    if x < 20:
        antwoord = input("Wilt u stoppen met spelen? ")
        if antwoord.lower() == "ja":
            x = 20
    x += 1

print("-----------------------------")
print("U heeft " + str(aantalGeraden) + " keer geraden")
print("U heeft " + str(score) + " keer goed geraden!")
print("-----------------------------")