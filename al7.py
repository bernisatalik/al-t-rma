#3 basamaklı, ilk iki basamaktaki sayıların toplamı ve son basamaktaki sayısı eşit olan sayılar ve adedi
adet=0
for a in range (100,1000):
    b=str(a)
    if int(b[0])+int(b[1])==int(b[2]):
        adet=adet+1
        print(b)
print(adet)
