########################
# 4.1
str1 = "İyi"

str2 = 'akşamlar'

dilek1 = str1 + str2

print("dilek1 :",dilek1)

dilek2 = str1 + ' ' + str2
print("dilek2 :", dilek2)

str3 = '123' # sayı değil

print(str(type(str3)))

# str3 sayı olmadığından alttaki işlem hata verir.
#str3 = str3 + 1

x = int(str3) + 1

print(x)

print(type(x))
########################

########################
# 4.2
name = input('Girdi : ')

print(name)

apple = input('Girdi : ')

#x = apple - 10 # hata verir

x = int(apple) - 10

print(x)
########################

########################
# 4.3

meyve = 'karpuz'

harf = meyve[1]
print(harf)


n = 3
w = meyve[n-1]
print(w)


z = 'abc'
print(z[2])
########################

########################
# 4.4
fruit = 'banana'

print(len(fruit))
########################

########################
# 4.5
isim = 'Arzu'
'Hello, {}'.format(isim)

soyisim = 'Arkın'

x = "{isim}'nun soyadı {soyisim} imiş. Cüneyt {soyisim}'la akraba mı acaba?".format(isim=isim, soyisim=soyisim)
print(x)


kilo = 5
fiyat = 6.5
meyve = "muz"
para = 5*6.5

"Pazardan kilosu {f} liradan {k} kg {m} aldım. {p} TL ödedim.".format(f = fiyat, 
    k = kilo, m = meyve, p = para)


kilo = 7
fiyat = 6.51
meyve = "muz"
para = kilo * fiyat

"Pazardan kilosu {f:0.4f} liradan {k} kg {m} aldım. {p:0.3f} TL ödedim.".format(f = fiyat, 
    k = kilo, m = meyve, p = para)

########################

########################
# 4.6
ifd = "Asya'dan Avrupa'ya geçtim."

print(ifd.upper())
print(ifd.lower())
print(ifd.capitalize())
print(ifd.count('a'))

########################