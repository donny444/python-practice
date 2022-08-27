answer = "elephant"
guess = ""
guess_count = 0
guess_limit = 5
out_of_guesses = False
print("This program is guessing game, you have 5 times limit to guess.")
while guess != answer and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("The animal which has trunk : ")
        guess_count += 1
        if  guess != answer and guess_count < guess_limit:
            print("Try again!")
    else:
        out_of_guesses = True
if out_of_guesses:
    print("YOU LOSE!")
else:
    print("YOU WIN!")