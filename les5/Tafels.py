N1 = 1
N2 = 1

import time


while N1 <= 50:
    Totaal = (N1*N2)
    print(N1, "x", N2, "=", Totaal)
    N2 = (N2 + 1)
    while N2 == 50:
        N1 = N1 + 1
        N2 = 1
        while N1 == 51:
            N2 = 50
            Totaal = (50*N2)
            print("50", "x", N2, "=", Totaal)
            N1 = 52

