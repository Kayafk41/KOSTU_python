su=float(input("ne kadar su harcadın:"))

if 10>su:
    total=su*30
elif 20>su>10:
    ksu=10*30
    osu=su-10*45
    total=ksu+osu
else:
    ksu=10*30
    osu=10*45
    bsu=(su-20)*70
    total=ksu+bsu+osu
print(total)