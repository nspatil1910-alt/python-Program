#Python Program to Find Simple Interest#
principle=float(input("Input the principle amount"))
time=int(input("Enter the time(years):"))
rate=float(input("Enter the rate"))
simple_interest=(principle*time*rate)/100
print("The simple interest is:",simple_interest)