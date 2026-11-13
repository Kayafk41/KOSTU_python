yas=float(input("yaşkaç:"))
gun=input("hangi gündeyiz:").strip().lower()

if gun== "çarşamba" :
    if 7>=yas: 
        print("beleş")
    else :
        print("120tl")
else :
    if 26>yas:
        print("160tl")
    else:
        print("220tl")
        