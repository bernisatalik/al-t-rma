#5 bas. ilk iki ve son iki rakamı birbirne eşit olan sayıların adedi
say=0
for a in range (10000,100000):
    b=str(a)
    if b[0]==b[3] and b[1]==b[4]:
        say+=1
print(say)
