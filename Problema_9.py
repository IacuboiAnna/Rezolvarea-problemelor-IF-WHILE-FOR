n=int(input("Dati numarul:"))
for numar_perfect in range(1,n+1):
    suma=0
    for divizor in range(1,numar_perfect):
        if(numar_perfect%divizor==0):
            suma+=divizor
    if (suma==numar_perfect):
        print(numar_perfect)