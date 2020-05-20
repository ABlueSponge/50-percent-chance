import random
condition = random.randint(1,2)
time = True
while time == True:
    answer = int (input("Enter Your Guess: ")) 
    if condition == answer:
        print("Good Job")
        time = False
        break
    elif condition != answer:
        print("Not quite. Try again")