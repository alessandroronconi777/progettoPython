print("decidi di che figura geometrica vuoi calcolare l'area:")
print("1 = quadrato")
print("2 = triangolo")
print("3 = rettangolo")
print("4 = cerchio")
print("5 = rombo")
scelta = input()

if int(scelta) == 1:
    print("inserisci lato quadrato: ")
    lato = input()
    area = int(lato) ** 2
    print("area: " + str(area))
elif int(scelta) == 2:
    print("inserisci base triangolo: ")
    base = input()
    print("inserisci altezza triangolo: ")
    altezza = input()
    area = (int(base) * int(altezza))/2
    print("area: " + str(area))
elif int(scelta) == 3:
    print("inserisci lato1 rettangolo: ")
    lato1 = input()
    print("inserisci lato2 rettangolo: ")
    lato2 = input()
    area = int(lato1) * int(lato2)
    print("area: " + str(area))
elif int(scelta) == 4:
    print("inserisci raggio cerchio: ")
    raggio = input()
    area = (int(raggio) ** 2 )* 3.14
    print("area: " + str(area))
elif int(scelta) == 5:
    print("inserisci diagonale maggiore: ")
    diagonaleMax = input()
    print("inserisci diagonale minore: ")
    diagonaleMin = input()
    area = (int(diagonaleMax) * int(diagonaleMin))/2
    print("area: " + str(area))
