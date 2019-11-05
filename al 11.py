#125, 200, 350 X'e bölününce hep aynı kalan çıkıyor. En büyük kalanı veren X

for x in range (1,350):
    if 350%x==200%x==125%x:
        c=x

print(c)
