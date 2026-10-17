n=int(input("Enter an interger"))
a=[]
for i in range(2,n+1):
    if(n%i==0):
        a.append(i)
    a.sort()
    print("Smallest divisor is:",a[0])
else:
     print("No divisor found")