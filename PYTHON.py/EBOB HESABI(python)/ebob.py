A=int(input("Büyük sayiyi girin:"))
B=int(input("Küçük sayiyi girin:"))
while B!=0:
    K = A % B
    A=B
    B=K
print("EBOB =",A)