

num = int(input('enter a number :')) 

def prime_numbers(num):
    primes =[]
    for i in range(2,int(num/2)):
        prime= True
        if i == 4 :
            continue
        for y in range(2,int(i/2)):
            
            if i%y ==0:
                prime= False
                break
        if prime ==True:
            primes.append(i)
    return primes  
     


def division_operation(num):
    divisors =[]
    prime = prime_numbers(num)
    while num != 1:
        
        for i in prime:
            if num % i ==0:
                divisors.append(i)
                num = num /i
                break
    return divisors

def print_the_product_of_prime_numbers(num):
    result = ""
    lenght =len(division_operation(num))
    item =division_operation(num)
    for i in range(lenght):
        result += str(item[i])  
        if i < lenght - 1:  
            result += '*' 

    print(result)


print_the_product_of_prime_numbers(num) 