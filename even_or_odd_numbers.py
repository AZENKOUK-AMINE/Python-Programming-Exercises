#this code is a simple code providing the user to enter a number and check whether it's an Even Or Odd number .


number = input("Enter a number :")

try:
    num = float(number)
    if num %2==0:
        print(f'{number } is an Even number ')
    else :
        print(f'{number } is an Odd number ')
except ValueError:
    print('invalid number !')
    