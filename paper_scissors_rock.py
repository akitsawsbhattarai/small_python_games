import random

def play():
    my_choice = input("Scissors(S) paper(P) rock(R) ?? ").lower()
    if my_choice == 's' or my_choice == 'p' or my_choice == 'r':
        computer_choice = random.choice(["s", "p", "r"])
        
        print(f"computer_choice: {computer_choice}")
        
        if computer_choice == my_choice:
            print("it/'s a tie")  
        elif win(my_choice, computer_choice):
            print('you win!!')
        else :
            print('computer win!!')
    else:
        print("choice is not valid")

#p>r s>p r>s 
def win(my_choice, computer_choice):
    if (my_choice == "p" and computer_choice == "r") or (my_choice == "s" and computer_choice == "p") or (my_choice == "r" and computer_choice == "s"):
        return True
    
while True:
    play()