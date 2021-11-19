print("Program Bilangan Terbesar Dari 3 Bilangan Yang Diinputkan")
A=int(input("Masukan Bilangan Pertama : "))
B=int(input("Masukan Bilangan Kedua : "))
C=int(input("Masukan Bilangan Ketiga : "))

if A > B and A > C :
    print(A,"Terbesar dari 3 bilangan yang diinputkan")
elif B > A and B > C :
    print(B,"Terbesar dari bilangan yang diinputkan")
else :
    print(C,"Terbesar dari 3 bilangan yanng diinputkan")
