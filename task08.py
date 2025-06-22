matn = "Python bu Python tili. Men Python o‘rganaman"
matn = matn.lower()
sozlar = matn.split()
s1 = sozlar[0]
s2 = sozlar[1]
s3 = sozlar[2]
n1 = sozlar.count(s1)
n2 = sozlar.count(s2)
n3 = sozlar.count(s3)
if n1 >= n2 and n1 >= n3:
    eng_kop = s1
elif n2 >= n1 and n2 >= n3:
    eng_kop = s2
else:
    eng_kop = s3

indeks = matn.find(eng_kop)

print("Eng ko‘p so‘z:", eng_kop)
print("Boshlanish indeksi:", indeks)
