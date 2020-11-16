#Se dau numerele naturale m si n, unde m<n. Sa se verifice daca n este o putere a lui m 
import math
m=int(input("Dati valoarea lui m:"))
n=int(input("Dati valoarea lui n:"))
if ((m<n) and (m>0) and (n>0)):
    s=math.log(n,m)
    p=round(s)
if ((m**p)==n):
    print(n, "este o putere a lui", m)
else:
    print(n, "nu este o putere a lui", m)