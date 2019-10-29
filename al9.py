#1-999 arasısayıların rakamları toplamı 9 dan küçük olan sayılar
for i in range (1,9):
    if i<9:
        print(i,end=" ")

for r in range(10,99):
    w=str(r)
    if int(w[0])+int(w[1])<9:
        print (w,end=" ")
        
for a in range (100,999):
    b=str(a)
    if int(b[0])+int(b[1])+int(b[2])<9 :
        print (b, end=" ")
