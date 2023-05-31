def deposit():
    a=str(input("Emter the account number"))
    acc="a"+".txt"
    f=open("acc","w+")
    z=str(0)
    f.write(z)
    f.close()
    f=open("acc","r")
    b=f.read()
    print("CURRENT BALANCE",b)
    c=int(input('Enter the amount to be deposited'))
    d=int(b)+c
    f.close()
    f=open("acc","w+")
    f.write(str(d))
    f.close
    f=open("acc","r")
    e=f.read()
    print("Balance",e)
def withdraw():
    a=str(input("Emter the account number"))
    acc="a"+".txt"
    f=open("acc","r")
    b=f.read()
    print("CURRENT BALANCE",b)
    c=int(input('Enter the amount to withdraw'))
    if int(b)>=c:
        d=int(b)-c
    f.close()
    f=open("acc","w+")
    f.write(str(d))
    f.close
    f=open("acc","r")
    e=f.read()
    print("Balance",e)
    
    
    

