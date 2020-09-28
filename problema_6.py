print("problema 6 Sobuleac Catalina")
n=9675
print("Ultima cifra a acestui numar este ", n%10)
print("Penultima cifra a acestui numar este ", n//10%10)
print("Restul impartirii acestui numar la 9 este ", n%9)
print("Catul impartirii acestui numar la 9 este ", n//9)
print("Suma cifrelor acestui numar este ", n//1000+n//100%10+n//10%10+n%10)
print("Rasturnatul acestui numar este ", n%10, n//10%10, n//100%10, n//1000, sep="")