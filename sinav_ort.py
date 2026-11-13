ara_sinav=float(input("ara sınav notu:"))
vize=int(input("vize notu:"))
final=int(input("final notu:"))

ara_agırlık=ara_sinav*0.20
vize_agırlık=vize*0.40
final_agırlık=final*0.40
total= ara_agırlık + vize_agırlık + final_agırlık 
print(total)