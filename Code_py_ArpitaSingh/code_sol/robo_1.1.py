#Q_1

#function that will accept two parameter

def function(lists,command):
    print('your command is to ',command)
    if command=='asc':
        lists.sort()      #why we cannot return direct sort lists : why it is applicable return(lists.sort())
        return lists
    elif command=='desc':
        lists.sort(reverse=True)
        return(lists)
    elif command=='none':
        return(lists)


n=int(input("enter no of number  "))
lists=[]
for i in range(0,n):
    lists.append(int(input("enter no ")))
print('entered lists is',lists)
parameter=str(input("enter your command(asc,desc,none) "))
print(function(lists,parameter))
