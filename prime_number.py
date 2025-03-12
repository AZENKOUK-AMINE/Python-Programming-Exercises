
#this code is to let the user to input to enter a number and check whether it is a prime number or not ....


num = input("Enter a number :")
prime = True

try:
    
    num2 = int(num)
    if(num == '1'):
        print('1 is not a prime number ')
    else :
        for i in range(2,int(num2/2)):
            if(num2 % i ==0):
                prime=False
                break
    
        print(f'{num} is prime 'if prime else  f'{num} is not prime ')

except ValueError:
    try:
        num2 = float(num)
        print('float number cannot be prime')
    
    except ValueError:
        print('invalid input')

    

    