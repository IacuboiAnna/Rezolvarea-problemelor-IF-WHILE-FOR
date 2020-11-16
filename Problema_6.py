#Se da numarul natural n. Sa se compare sumele S1 si S2, unde:
#a)S1=1^3+2^3+...+n^3 si S2=(1+2+...+n)^2
#b)S1=3(1^2+2^2+...+n^2) si S2=n^3+n^2+(1+2+...+n)
n=int(input("Dati valoarea lui n:"))
s1a=0
ss=0
s2a=0
ss1=0
s1b=0
s2b=0
for i in range(1,n+1):
    s1a+=(i**3)
    ss+=i
    s2a=(ss**2)
    ss1+=(i**2)
    s1b=3*ss1
    s2b=(n**3)+(n**2)+ss

if (s1a>s2a):
    print("a)S1>S2")
if (s1a==s2a):
    print("a)S1=S2")
if (s1a<s2a):
    print("a)S1<S2")

if (s1b>s2b):
    print("b)S1>S2")
if (s1b==s2b):
    print("b)S1=S2")
if (s1b<s2b):
    print("b)S1<S2")