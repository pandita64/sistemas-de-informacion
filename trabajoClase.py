num = []
cont = 0
while cont < 6:
    try:
        n = int(input(f"Ingrese el número {cont+1}: "))
        num.append(n)
        cont += 1
    except TypeError:
        print("Por favor, ingrese un número válido.")
        
multiplos_Dos = []
cont1 = 0
while cont1 < len(num):
    if num[cont1] % 2 == 0:
        multiplos_Dos.append(num[cont1])
    cont1 += 1 
    
print("Números múltiplos de dos:")
print(multiplos_Dos)

