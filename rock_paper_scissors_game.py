import random

items = ['p','r','s']
random_choice= random.choice(items)



print(random_choice)
user_score = 0
computer_score=0
    

quit="t"
 



while True:
    user_choice= input("choise! Rock :R , Scissors : S , paper :P , score:score , quit :q ::").lower()
    random_choice= random.choice(items)
    if user_choice  in items or user_choice=="score" or user_choice=='q':
        if user_choice=="q":
            print('game ended!')
            print("your score :",user_score,"- computer score",computer_score)
            break
        elif user_choice == 'score':
            print("your score :",user_score,"- computer score",computer_score)
        elif user_choice == random_choice:
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            pass
        elif user_choice == 'r' and random_choice=='p':
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            computer_score+=1
        elif user_choice == 'r' and random_choice=='s':
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            user_score+=1
        elif user_choice == 'p' and random_choice=='s':
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            computer_score+=1
        elif user_choice == 'p' and random_choice=='r':
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            user_score+=1
        elif user_choice == 's' and random_choice=='r':
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            computer_score+=1
        elif user_choice == 's' and random_choice=='p':
            print(f'your choice :{user_choice} - coputer choice :{random_choice}')
            user_score+=1 
    else :
        print("Invalid input!")
    
    

    
