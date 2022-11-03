from cgitb import reset
import datetime

def main():
        Datum = datetime.datetime.now()

        m = (Datum.month)
        d = (Datum.day)

        print("Hello You! Ik ben Wessel")

        username = input("Wie ben jij?")
        print("Hallo " + username )

        txt1 = "De datum van vandaag is {}"
        print(txt1.format(Datum.strftime("%x")))

        x = input("In welk jaar ben je geboren? ")
        y = input("In hoeveelste maand ben je geboren? ")
        z = input("Op welke dag van die maand ben je geboren? ")

        y = int(y)
        z = int(z)

        if y < m:
            output = (int(x))
            output = (str(2022-output))
        elif y == m:
            if z > d:
                output = (int(x))
                output = (str(2021-output))
            else:
                output = (int(x))
                output = (str(2022-output))
        else:
            output = (int(x))
            output = (str(2021-output))

        txt2 = "Je bent dus {} jaar oud"
        print(txt2.format(output))

main()

if input("Zou je dit opnieuw willen proberen? Y/N").lower().startswith('y'):
    main()
else:
    print("oké dan")
