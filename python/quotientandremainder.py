a=int(input("Enter first Number :"))
b=int(input("Enter Second Number :"))

if b != 0:
    quotient=a//b
    remainder=a%b
    print("Quotient:",quotient)
    print("Remainder:",remainder)
    
    else:
        print("cannot divide by zero is not allowed")
