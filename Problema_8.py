#Se dau numerele reale pozitive a,b,c. Sa se verifice daca exista un triunghi ale carui laturi au
#lungimile (in aceeasi unitate de masura) egale cu a,b,c. In caz afirmativ, sa se determine tipul 
#triunghiului: echilateral, isoscel, scalen. 
a=eval(input("Dati prima latura a triunghiului in cm:"))
b=eval(input("Dati a doua latura a triunghiului in cm:"))
c=eval(input("Dati a treia latura a triunghiului in cm:"))
if ((a>0) and (b>0) and (c>0)):
    if ((a<(b+c)) and (b<(a+c)) and (c<(a+b))):
        if ((a==b) and (b==c) and (a==c)):
            print("Triunghi echilateral")
        if ((a==b) and (a!=c)) or ((a==c) and (a!=b)) or ((b==c) and (b!=a)):
            print("Triunghi isoscel") 
        if ((a!=b) and (a!=c) and (b!=c)):
            print("Triunghi scalen")
    else:
        print("Nu exista asa triunghi")
else:
    print("Lungimile sunt numere pozitive") 