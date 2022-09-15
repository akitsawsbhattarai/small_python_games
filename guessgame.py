import random
print("write a range of number: ")
x = int(input("from : "))
y = int(input("to : "))
random_number = random.randint(x,y)

guessed_number = 0
while guessed_number != random_number:

    try :
        guessed_number = int( input(f"Guess a number between {x} and {y}: "))
        
        if guessed_number < random_number :
            print('oops! too low')
        elif  guessed_number > random_number :
            print('oops! too high')
    except :
        print("please provide valid number!!")
    

print(f'congrats! {guessed_number} is correct')
