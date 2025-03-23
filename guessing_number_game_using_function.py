import random 

def check_input(user_guess , computer_guess):
        if  user_guess == computer_guess: 
            return True
        elif 0<= user_guess <= 100 :
            if user_guess< computer_guess:
                print('the value is greater than your guess  ')
               
            elif user_guess> computer_guess:
                print('the value is less than your guess . re-enter a value ')
                
           
        
        
 
        
computer_guess = random.choice(range(1,101))
user_guess = int(input('Guess a number between 1 and 100 :'))
while True:
    try :     
        
        
        print(computer_guess)
        if check_input(user_guess ,computer_guess):
            print('Good job ! the value is ',computer_guess)
            break
        else :
            user_guess=int(input('Guess again :'))
        
    except ValueError:
        
        print('please enter an integer  ')
        user_guess=int(input('Guess again :'))