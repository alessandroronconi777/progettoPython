dividendo = int(input("dividendo: "))
divisore = int(input("divisore: "))

quoziente = 0
resto = 0

if dividendo == 0:
    print("il quoziente e il resto sono uguali a 0")
else:
    if divisore == 0:
        print("divisione per zero impossibile")
    else:
        if divisore < 0:
            x = -divisore
        else:
            x = divisore
        while dividendo >= x:
            dividendo = dividendo - x
            quoziente = quoziente + 1

        resto = dividendo
        print("il quoziente è: " + str(quoziente) + " e il resto è: " + str(resto))
