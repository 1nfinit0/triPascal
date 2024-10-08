def printPascalRow(row):
    plot = ""
    space = "     "
    for i in range(row+1):
        numero = str(combinacion(row, i))
        plot = plot+numero+space[0:6-len(numero)]
    return plot

def combinacion(n,k):
    if k > n:
        return "XD"
    if k == n or k == 0:
        return 1
    if k == 1 or k == n-1:
        return n

    if k > n/2:
        k = n - k

    numerador = 1
    for i in range(k):
        numerador = numerador*(n - i)

    denominador = 1
    for i in range(k):
        denominador = denominador * (i + 1)

    return int(numerador/denominador)

def triPascal(rows):
    space = "   "
    for i in range(rows+1):
        print("\n",space*(rows - i),printPascalRow(i))

if __name__ == "__main__":
    print("\nBienvenido al generador del Triángulo de Pascal!\n")
    rows = int(input("Generar hasta la fila:   ") )
    triPascal(rows);
    #test:
    #print(printPascalRow(10))
    #print(combinacion(14,5)) 
    
