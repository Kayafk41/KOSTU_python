yuzkm=float(input("100 kmde kaç litre yakıt yakar:"))
gidlecek_yol=int(input("gidilecek yol kaç km:"))
yakit_fiyat=float(input("yaktın litre fiyatı:"))

gereken_yakit=gidlecek_yol/yuzkm
tota_fiyat=gereken_yakit*yakit_fiyat

print(gidlecek_yol,"km için gereken yakıt:\t",f"{gereken_yakit: 2.f}","\ntoplam maaliyet:\t",f"{tota_fiyat: .2f}")