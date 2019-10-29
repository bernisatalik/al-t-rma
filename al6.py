#4 basamaklı sayılarda ilk rakamı son rakamdan büyük olan sayıların adedi
i=0
for a in range (1000,9999):
    b=str(a)
    if b[0]>b[3]:
        i=1+i
print(i)
