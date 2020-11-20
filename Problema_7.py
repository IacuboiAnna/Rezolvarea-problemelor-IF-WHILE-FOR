n=int(input("Introduceti varsta lui Mihai, pana la 20 de ani:"))
s=1
for i in range(1,n+1):
    s=(s*2)+i

print("La varsta de", n, "ani Mihai avea o suma de", s, "dolari")

s=1
v_100=0
for i in range(1,n+1):
    while (s<=100):
        s=(s*2)+i
        v_100+=1

print("La varsta de", v_100, "ani Mihai avea o suma mai mare ca 100 de dolari")