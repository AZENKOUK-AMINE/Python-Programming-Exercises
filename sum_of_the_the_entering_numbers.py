
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
        


#second methode just change i from string to integer and then add it to total:

# number = int(input('Enter an integer  :'))

# count= len(str(number))


# def sum(number):
#     total=0
#     for i in str(number):
#         total+=int(i)
#     return total


# print("the sum of the input digits is " + str(sum(number)))


        
        
    
    
    


