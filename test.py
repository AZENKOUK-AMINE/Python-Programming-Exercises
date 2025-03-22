

# t = [(1,2),(1,4)]

# def finding_the_splot(data):
#     lenght= len(data)
#     sum_x=0
#     sum_y=0
#     for i in range(0,lenght):
#         sum_x+=data[i][0]
#         sum_y+=data[i][1]
#     return sum_x , sum_y

# print(finding_the_splot(t))


# number = int(input('Enter an integer  :'))

# count= len(str(number))


# def sum(number):
#     total=0
#     for i in str(number):
#         total+=int(i)
#     return total
    


# print("the sum of the input digits is " + str(sum(number)))


# def get_months():
#     month = int(input("enter a month :"))
#     while 12< month or month< 1:
#         month = int(input("re-enter the month :"))
        
#     return month  

# get_months()



# lst =list(range(1,100))
# lst=list(x**3 - x**2 +1 for x in range(0,10))


# # for i in range(len(lst)-1,-1,-1):
# #     print(lst[i] ,end=" "  )
    
# # for i in range(len(lst)):
# #     print(lst[-1-i] ,end=" "  )

# print(lst)


# write a function to get all the prime number of another list 
#write a function to find all prime numbers in 1-100


# prime = True
 
# def prime_numbers(num): 
#     primes_list=[] 
#     for i in num:
#         num1 =i
#         for j in range(2,int(i/2)+1):
#             if(i % j ==0):
#                 prime=False
#                 break
#         else:
#             if i == 1:
#                 continue
#             else:
#                 primes_list.append(i)
        
#     return primes_list

# print(prime_numbers([1,4,5,8,8,7,6,11]))

# #second task :
# def prime_numbers(num):
#     primes =[]
#     for i in range(2,int(num/2)):
#         prime= True
#         if i == 4 :
#             continue
#         for y in range(2,int(i/2)):
            
#             if i%y ==0:
#                 prime= False
#                 break
#         if prime ==True:
#             primes.append(i)
#     return primes  

# print(prime_numbers(100))
######first h.w
num1 = int(input("Enter the first number :"))
num2 = int(input("Enter the Second number :"))

print("the sum is :",num1+num2 , "and the product is :" , num1*num2)

def hex_num(num):
    return hex(num)

def bin_num(num):
    return bin(num)


def octal_num(num):
    return oct(num)

print(f'the hex of first number is : {hex_num(num1)}')
print(f'the bin of first number is : {bin_num(num1)}')
print(f'the oct of first number is : {octal_num(num1)}')
print(f'the hex of  second is : {hex_num(num2)}')
print(f'the bin of  second is : {bin_num(num2)}')
print(f'the oct of  secnd is : {octal_num(num2)}')


num3=int(input("enter a positive number with thre digits "))

def sum(number):
    total=0
    for i in str(number):
        total+=(int(i)**3)
    return total


if num3 >0:
    print(sum(num3))
else:
    print('the number is not positive ')

    