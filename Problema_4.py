from fractions import Fraction
a=int(input("Dati numaratorul primii fractii:"))
b=int(input("Dati numitorul primii fractii:"))
c=int(input("Dati numaratorul fractiei a doua:"))
d=int(input("Dati numitorul fractiei a doua:"))
if ((b!=0) and (d!=0)):
    print("Suma este:", Fraction(a,b)+Fraction(c,d))
    print("Produsul este:", Fraction(a,b)*Fraction(c,d))
else:
    print("Numitorul unei fractii este un numar nenul")