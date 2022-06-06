#q_4
#fun_1 accept string
def fun(str):
    b=''
    for i in str:
        b=(b+i*2)
    return b

string = (input("enter your string "))
print(fun(string))