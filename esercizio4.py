print("inserisci quanti numeri vuoi confrontare: ")
n = int(input())

numero = int(input("inserisci primo numero da cronfrontare: "))

max = numero

for i in range(1, n, 1):
    numero = int(input("nuovo numero da confrontare:"))

    if max < numero:
        max = numero

print("il numero massimo è: " + str(max))