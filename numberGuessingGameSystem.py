import random
num = random.randint(1,100)
# print(num)
tries = 0
while 1:
    guess = int(input("Guess a number in between 1-100 : "));
    tries += 1;
    if guess == num:
        print("Congratulation guess the corrent number");
        print("You guess the number in",tries,"tries")
        break;
    elif num > guess :
        print("Guess higher");
    else:
        print("Guess lower")
