a=str(input("Enter the file name  "))
acc="a"+".txt"
f=open("acc","r")
b=f.read()
data=b.split()
c=max(data,key=len)
print(c)
