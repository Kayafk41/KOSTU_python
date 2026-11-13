urun_sayisi = int(input("elimizde kaç ürün var:"))
koli_kapasitesi = int(input("1 koliye kaç ürün sığar"))

tam_koli = urun_sayisi // koli_kapasitesi
kalan = urun_sayisi % tam_koli

print("gerekli olan koli sayısı:" , 1+tam_koli )
print("son kolideki ürün sayısı:" , kalan)
