import datetime

def leeftijd(jaar, maand, dag):

    Y1 = datetime.datetime(jaar, maand, dag)
    Y2 = datetime.datetime.now()
    dag = Y2-Y1
    return dag

def main():
    print("noteer geboortedatum in nummers")
    x = input("jaar geboorte: ")
    y = input("maand geboorte: ")
    z = input("dag gebooorte: ")
    
    dag = leeftijd(int(x), int(y), int(z))
    
    txt = "het is {} dagen geweest sinds je geboorte"
    print(txt.format(dag.days))

    print("wil je dit opnieuw doen?")
    ans = input("> ")
    if ans.lower().startswith("y"):
        main()

main()