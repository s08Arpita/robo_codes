#Q_9
string=input("enyer any string ")
list=([char for char in string])
list.sort()
list_2=''.join([char for char in list])
print(list_2)
