#Q_5
#random
import numpy

rolls=numpy.random.randint(low =1,high=99,size=100)
num=rolls.tolist()

print("array of 100 no \n",num)

for n in num:
    if num.count(n) ==2:
        print("a no which is duplicate \n"+str(n))
        break