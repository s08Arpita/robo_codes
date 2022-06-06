#Q_3
#function have to accept three parameter (int,command,int)

def function(par_1,par_2,par_3):
    if par_2=='+':
        return(par_1+par_3)
    elif par_2=='-':
        return(par_1-par_3)
    elif par_2=='*':
        return(par_1*par_3)
    elif par_2=="/":
        return(par_1/par_3)


parameter_1=(int(input("enter first no ")))
parameter_2=(str(input("type your command (+,-,*,/ ) ")))
parameter_3=(int(input("enter second no ")))
print(function(parameter_1,parameter_2,parameter_3))