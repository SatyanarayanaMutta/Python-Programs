num1=int(input("num1="))
num2=int(input("num2="))

while(num1 != num2):
    if(num1>num2):
        num1-=num2
    else:
        num2-=num1

print("GCD of given numbers is:",num2)
