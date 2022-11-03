def bereken_maandkosten(km_per_maand):
    verzekering_per_maand = 23
    benzine_kosten_per_liter = 1.54
    liter_per_kilometer = 0.2
    maandkosten = ((km_per_maand*liter_per_kilometer*benzine_kosten_per_liter) + verzekering_per_maand)
    return maandkosten

kost = bereken_maandkosten(30)

print(kost)