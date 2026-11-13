import math
fiyat=float(input("pizzanın fiyatı nedir:"))
cap=float(input("pizzanın çapı nedir:"))
yaricap=cap/2
alan=math.pi * yaricap**2
birim_fiyat=alan/fiyat
print("pizzanın 1cmsi için ödenen tutar:"f"{birim_fiyat: .2f}")