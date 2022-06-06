#Q_6
#print all prime no 

ran=int(input("enter the maximum range "))
print(2)
for n in range(1,ran):
    for i in range(2,n):
        if n%i==0:
            break
        if i==n-1:
            print(n )
   