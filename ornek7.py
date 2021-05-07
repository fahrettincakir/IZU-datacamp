########################
# 7.1

arkadaşlarım = ["Ali","Güven","Veli"]

print("Birinci arkadaşım, ", arkadaşlarım[0])

print("İkinci arkadaşım, ", arkadaşlarım[1])

print("Üçüncü arkadaşım, ", arkadaşlarım[2])

########################
# 7.2
çantadakiler = ["kalem","kolonya","selpak","cüzdan","kağıt"]


çantadakiler.remove("kalem")
print("Çantanızda kalanlar.", çantadakiler)

çantadakiler.remove("selpak")
print("Çantanızda kalanlar.", çantadakiler)

çantadakiler.insert(1,"portakal")
print("Çantanızda kalanlar.", çantadakiler)

çantadakiler.clear()
print("Çantanızda kalanlar.", çantadakiler)

if not çantadakiler:
    print("Tüm çantayı boşalttınız.")
else:
    print("Çantanızda birşey var.")
########################

########################
# 7.3
t = [9, 41, 12, 3, 74, 15]

print(t[0:3])

print(t[:4])

print(t[3:])

print(t[:])

print(t[::-1])

########################

########################
# 7.4

x = (1,2,3,4)

print(x[2:])

print(x[::-1])

x[2] = 12 # hata verir.