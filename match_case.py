boy=input("kahveniz hangi boy olsun:(k:küçük , o: orta , b: büyük)")

match boy:
    case "k":
        ad , fiyat = "küçük" , 70
    case "o":
        ad , fiyat= "orta" , 85
    case "b":
        ad , fiyat = "büyük" , 100
    case _:
        ad , fiyat = "tanımsız" , 0

if fiyat ==0 :
    print(boy , "diye bir boy yok")
else:
    print(ad ,"boy kahveniz:", fiyat, "tl")
