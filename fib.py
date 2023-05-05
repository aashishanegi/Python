def FibR(n):  
   if n <= 1:  
       return n  
   else:  
       return(FibR(n-1) + FibR(n-2))
def Sum(n):
    if n == 1:
        return 1
    else:
        return n + Sum(n-1)


n = int(input("Enter Number: "))
if n <= 0: 
   print("Please enter a positive integer")  
else:  
    print("Sum of Number",Sum(n))
    print("Fibonacci sequence:")  
    for i in range(n):  
       print(FibR(i))
