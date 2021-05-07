########################
# 9.1
n = 9

while n>0:
    print(n)
    n = n - 1

print("Roket kalktı!")

########################

########################
# 9.2
n = 5

while n > 0:
    print("İn")
    print("Çık")
    

print("Yoruldum!")

#######################
# 9.3
n = 0

while n > 0:
    print("İn")
    print("Çık")

print("Yoruldum!")

########################
# 9.4

while True:
    line = input("Sihirli kelimeyi söyleyin >")
    if line == "tamam":
        break
    
    print(line)

print("Döngüden çıktık. Çok şükür!")

while True:
    line = input(">")
    if line[0] == "#":
        continue
    if line == "tamam":
        break
    print(line)

print("Döngüden çıktık. Çok şükür!")

########################

########################
# 9.5

for i in [5,4,3,2,1]:
    print(i)

print("Roket kalktı!")

########################
# 9.6
arks = ["Ali","Hasan","Hüseyin"]

for ark in arks:
    print("Bayramın kutlu olsun,", ark)

print("Tamam!")
########################

########################
# 9.7

toplam = 0
for i in [*range(1, 11)]:
    toplam = toplam + i

print(toplam)

toplam = 0
for i in [*range(11)]:
    toplam = toplam + i

print(toplam)

for i in range(7,0,-1):
    print(i)

print("Roket kalktı!")

#######################

#######################
# 9.8
print("Başla...")

for sayı in [9,41,12,3,74,15]:
    if sayı > 20:
        print("Büyük sayı ", sayı)

print("Son...")
########################