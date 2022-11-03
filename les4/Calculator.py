def Bereken(a, b, op):

                        #checken welke operator je hebt gekozen
    if op == "+":           #Je kiest voor optellen
        result = a+b        #Bereken de uitkomst
    elif op == "-":         #Je kiest voor aftrekken
        result = a-b        #Bereken de uitkomst
    elif op == "/":         #Je kiest voor delen
        result = a/b        #Bereken de uitkomst
    elif op == "*":         #Je kiest voor vermenigvuldigen
        result = a*b        #Bereken de uitkomst
    elif op == "%":         #Je kiest voor restwaarde na deling (modulo)
        result = a%b        #Bereken de uitkomst
    else:                   #Je hebt geen geldige berekening gekozen
        result = 0          
    return result

print(Bereken(10, 10, "+"))         
print(Bereken(20, 10, "/"))
print(Bereken(10, 70, "*"))
print(Bereken(10, 190, "+"))
print(Bereken(50, 10, "%"))
