numeroParole = int(input("quante parole vuoi inserire: "))

parola = "zz"

for i in range(numeroParole):
    parolaNuova = input("inserire una parola ")

    if parolaNuova < parola:
        parolaSalvata = parola
        parola = parolaNuova + "," + parolaSalvata
        
print(parola)
