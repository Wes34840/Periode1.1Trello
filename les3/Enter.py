age = input("Goedenavond, hoe oud bent u? ")

if int(age) >= 18:
    if input("Mag ik uw ID zien? ").lower().startswith("j"):
        print("Kom maar verder")
    else:
        print("Geen ID, geen entree")
    
else:
    print("Dan bent u te jong, kom terug wanneer u boven de 18 bent")