#Q_2
def atm(no):
    l = len(no)
    b = '*'*(l-4)+no[-4:]
    return b
    
atm_no=(input("enter your atm no "))
print("your card no ",atm(atm_no))

