
number = int(input('Enter an integer  :'))

count= len(str(number))


def sum(number):
    total=0
    for i in str(number):
        rest = number%10
        total+=rest
        number=number//10
        
    return total


print("the sum of the input digits is " + str(sum(number)))
        
        
        
        
    
    
    


