mesafe = float(input("kilometre olarak ne kadar mesafe gittin:"))
sure_dk = float(input("peki kaç dakikada gittin:"))

sure_saat = sure_dk / 60        #ortalama hız km/saat olarak hesaplanır
orthiz = mesafe / sure_saat     
tempo = sure_dk / mesafe
print(mesafe , "kilometrede ortalama hızınız:" ,f"{orthiz:.2f}" ,"\ntemponuz:" , f"{tempo: .2f}")