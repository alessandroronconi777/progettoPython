print("inserisci 3 numeri interi: ")
numero1 = input("Inserisci il primo numero: ")
numero2 = input("Inserisci il secondo numero: ")
numero3 = input("Inserisci il terzo numero: ")
massimo = 0

if int(numero1) >= int(numero2) and int(numero1) >= int(numero3):
    massimo = numero1
elif int(numero2) >= int(numero1) and int(numero2) >= int(numero3):
    massimo = numero2
else:
    massimo = numero3

print("il numero massimo è: " + str(massimo))