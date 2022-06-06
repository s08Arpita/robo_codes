#Q_8


string=input("enter your text here ")
l=len(string)
n=0
for i in range(l):
 if string[i].isdigit():
        n=n+int(string[i])
        
print(n)