#Kullanıcı Girdisi 1
isim = input("Adınız nedir? \n")
print("Merhaba," + " " + isim)

#Kullanıcı girdisi 2
sayı_str = input("Numaranız nedir? ")
print("Numaranızı " + sayı_str + " olarak girdiniz.")

# Metin dosyası oku
name = input("Enter file name : ") # Dosya adını uzantısıyla birlikte girin.
handle = open(name,"r", encoding="utf8")
text = handle.read()
handle.close()

sözcükler = text.split()
print(sözcükler)