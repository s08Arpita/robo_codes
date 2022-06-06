#Q_7
#random
import numpy as numpy

rolls=numpy.random.randint(low =1,high=99,size=100)
num=rolls.tolist()
num_copy=num.copy()
freq=[]
print("array of 100 no \n",num)
for n in num:
    c=int(num.count(n))
    freq.append(c)
    num.remove(n)
max_f=max(freq)
for n in num_copy:
    if num_copy.count(n)==max_f:
        print("highest frequecy element "+str(n))
        break


    