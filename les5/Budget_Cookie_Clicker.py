import os


import os

cookie = 0
answer = "ja"

while answer.lower().startswith("ja"):
    answer = input("Wil je klikken? ")
    if answer.lower().startswith("ja"):
        cookie = cookie + 1



os.system("cls")
txt = "Game over, je hebt in totaal {} keer het koekje geklikt"
print(txt.format(cookie))