import math

yaricap = float(input("tankın yarıçapını metre cinsinden giriniz:"))
yukseklik = float(input("yüksekliği metre cinsinden giriniz:"))

hacim = math.pi * yaricap**2 * yukseklik 
litre = hacim * 1000

print("tankın hacmi:\nmetreküp cinsinden:" ,f"{hacim:.2f}" , "\nlitre cinsinden:",f"{litre:.2f}" )