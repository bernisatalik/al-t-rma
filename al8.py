#3 basamaklı en az 2 basamağındaki rakamları aynı sayıların adedi
say=0
for a in range (100,1000,2):
    b=str(a)
    if b[0]==b[1]:
        say+=1
    elif b[0]==b[2]:
        say+=1
    elif b[1]==b[2]:
        say+=1
print (say)
