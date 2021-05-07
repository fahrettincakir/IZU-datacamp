########################
# 11.1
def oku(fname):
    fin = open(fname)
    for line in fin:
        word = line.strip()#kelime başı ve sonundaki görünmeyen karakterleri çıkarır
        if len(word) >= 20:
            print(word,len(word))
    
    fin.close()


oku("words.txt")

########################

########################
# 11.2

with open("test.txt",'w+',encoding = 'utf-8') as f:
   f.write("birinci satır\n")
   f.write("İkinci satır\n")
   f.write("Üçüncü satır\n")
########################

########################
# 11.3

with open("test.txt",mode='a+',encoding = 'utf-8' ) as f:
   f.write("Bir varmış\n")
   f.write("Bir yokmuş\n")
########################