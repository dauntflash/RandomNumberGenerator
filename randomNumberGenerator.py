import random

def limits():
    max_value = 100
    min_value = 1
    num= random.randint(min_value, max_value)
    return num

num=int (limits())
print(num)

guess=input("I am thinking of a number between 1 and 100, guess the number: ")

while True:
    if guess.isdigit() and int(guess) <= 100 and int(guess) != 0:
        guess=int (guess)
        break
    else:
        guess=input("Invalid input, please enter a digit number between 1 and 100: ")


diff = num-guess
diff = abs(int (diff))

counter=0
while True:
    counter+=1
    if diff >= 20:
        new=int(input("You are too far,, guess again: "))
        diff = num-new
        diff=abs(int(diff))
    elif diff < 20 and diff >= 10:
        new=int(input("A little far, guess again: "))
        diff = num-new
        diff = abs(int(diff))
    elif diff >=5 and diff < 10:
        new=int(input("You are close, guess again: "))
        diff = num-new
        diff = abs(int (diff))
    elif diff >=1 and diff <= 3:
        new=int(input("You are almost there, one more guess: "))
        diff = num-new
        diff = abs(int (diff))
    elif diff == 0:
        print("You've got it with a total of",counter,"guesses...")
        break