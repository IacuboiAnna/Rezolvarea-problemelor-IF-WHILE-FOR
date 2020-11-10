#Sa se calculeze 1!+2!+3!+...+n!(n>1)
n=int(input("Dati n:"))
p=1
s=0
for i in range(1,n+1):
    p*=i
    s+=p

print(s)