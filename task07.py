matn = '"Men Python dasturlash tilini o‘rganaman", "Python"'
soz = "Python"
boshlanish_indeksi = matn.find(soz)

if boshlanish_indeksi != -1:
    print(f'"{soz}" so‘zi matnda topildi.')
    print(f'Boshlanish indeksi: {boshlanish_indeksi}')
else:
    print(f'"{soz}" so‘zi matnda topilmadi.')
