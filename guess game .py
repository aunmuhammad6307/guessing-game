


my_name = input("Enter your name: \t")
tries = 0
total_tries = 5
import random
number = random.randint(1,50)
print(f"Well {my_name}, \nyou only think number between 1 and 50. ")
try:
    for tries in range(5):
        print(f"let go! \nPlay game {my_name}.")
        guess = input("Take a guess.\t")
        
        if guess.isnumeric():
            guess = int(guess)
        
           
            if guess < number:
                print(f"{my_name} your guess is less then the guess number. \nPlease enter some big value.")
                total_tries = total_tries - 1
                print(f"{my_name} your tries left are {total_tries} ")
            elif guess > number:
                print(f"{my_name} your guess is greater then the guess number. \nPlease enter some small value.")
                total_tries = total_tries - 1
                print(f"{my_name} your tries left are {total_tries} ")
            elif guess == number:
                break
            else:
                print("Invalid input!. Please enter integer value only.")
        else:
            print("Invalid input!. Please enter integer value only.")
        
    if guess != number:
        print(f"Nobe, {my_name}. \n These numbers {guess} that your are think was not a guess number. \n The guess number is {number}.")
    elif guess == number:
        print(f"GOOD JOB!, {my_name}. \nCongratuation. You guess my number in {number}. ")
except ValueError:
    print('Invalid input!. Please enter integer value only.') 



    
        





