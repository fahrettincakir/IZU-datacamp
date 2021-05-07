########################
# 6.1
soyisim = input("Soyisminiz nedir? ")


if soyisim[0] < "K":
    print("Sınava gireceğiniz sınıf EK 101.")
elif soyisim[0] >= "K":
    print("Sınava gireceğiniz sınıf EK 201.")

########################

########################
# 6.2
sayı = int(input("3 ile başlayan üç basamaklı bir pozitif bir sayı girin : "))


if sayı < 100:
    print("Yanlış. İki basamaklı bir sayı girdiniz.")
elif sayı < 0:
    print("Yanlış. Negatif bir sayı girdiniz.")
elif sayı > 100 and sayı < 300:
    print("Yanlış. 100 ile 299 arasında bir sayı girdiniz.")
elif sayı > 400 and sayı < 1000:
    print("Yanlış. Sayınız çok büyük. 300 ile 400 arasında olmalı.")

########################