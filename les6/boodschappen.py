import os

boodschappen = []

while True:
    if len(boodschappen) :
        print("Je boodschappenlijst is nu: ", boodschappen)
    else:
        print("Je boodschappenlijst is leeg")
    print("Wil je iets toevoegen of verwijderen?")
    ans = input("> ")
    if ans.lower().startswith("t"):
        print("Wat wil je toevoegen?")
        ans = input("> ")
        boodschappen.append(ans)
        os.system("cls")
    elif ans == "end":
        os.system("cls")
        break
    else:
        print("wat wil je verwijderen? ")
        ans = input("> ")
        boodschappen.pop(boodschappen.index(ans))
        os.system("cls")

print("je boodschappenlijst is: ", boodschappen)