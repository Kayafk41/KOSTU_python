uzunluk=float(input("uzunuk(cm):"))
genişlik=float(input("genişlik(cm):"))
derinlik=float(input("derinlik(cm):"))

hacim= uzunluk*genişlik*derinlik
hacimlit=hacim/1000
hacim_degisim=hacimlit/4
print("litre hacim:\t", hacimlit , "\ndeğişmesi gereken miktar:\t" , f"{hacim_degisim: .2f}")