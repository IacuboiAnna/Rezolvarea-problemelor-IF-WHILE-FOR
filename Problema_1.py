#Se da numarul natural n, n apartine {28,29,30,31}. 
#Sa se afiseze denumirile lunilor cu numarul de zile n.
#De exemplu, pentru n=30, se va afisa:
#aprilie, iunie, septembrie, noiembrie
n=int(input("Dati numarul de zile:"))
if ((n>=28) and (n<=31)):
    if n==28:
        print("februarie, intr-un an obisnuit")
    if n==29:
        print("februarie, intr-un an bisect")
    if n==30:
        print("aprilie, iunie, septembrie, noiembrie")
    if n==31:
        print("ianuarie, martie, mai, iulie, august, octombrie, decembrie")
else:
    print("Nu exista luni cu asa numar de zile!")