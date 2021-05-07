########################
# 10.1
def selam():    # fonksiyon imzası/deklarasyon başı
    print("selam")
    print("nbr?")

def selam2(x):
    print(x)
    print('nbr?')



selam()

selam('Ali')
selam2('Ali')

########################

#######################3
# 10.2

def selam(lang):
    
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    elif lang == "tr":
        print("Merhaba")
    else:
        print("Hello")


selam("en") # çağırma
 
selam("es") # çağırma

selam("fr") # çağırma

def selam3():
    return("Hello ")

print(selam3(), "Ahmet")
print(selam3(), "Ali") 

########################

########################
# 10.3
def foo(a,b):
    x = a
    y = b
    return(x*y + y)

q = foo(3,4)
########################

########################
# 10.4
DAKİKA_SANİYE = 60

def kaçtamdakika(saniye):
    dk = saniye // DAKİKA_SANİYE
    
    return(dk)

print(kaçtamdakika)
print(saniye)#hata verir