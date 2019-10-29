import math
sum=0
for i in range (1,1000000):
    sum+=1/(i**2)
p=math.sqrt(6*sum)
print(p)
