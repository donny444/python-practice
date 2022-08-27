print("------Alphabet Guessing Game------")
def cond_1():
    secret_alp_1 = "a"
    guess_1 = ""
    out_of_guesses = False
    guess_count_1 = 0
    guess_limit = 3
    while guess_1 != secret_alp_1 and not(out_of_guesses):
        if guess_count_1 < guess_limit:
            guess_1 = input("eleph_nt : ")
            guess_count_1 += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses, YOU LOSE!")
    else:
        cond_2()
def cond_2():
    secret_alp_2 = "g"
    guess_2 = ""
    out_of_guesses = False
    guess_count_2 = 0
    guess_limit = 3
    while guess_2 != secret_alp_2 and not(out_of_guesses):
        if guess_count_2 < guess_limit:
            guess_2 = input("_irrafe : ")
            guess_count_2 += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses, YOU LOSE!")
    else: 
        cond_3()
def cond_3():
    secret_alp_3 = "c"
    guess_3 = ""
    out_of_guesses = False
    guess_count_3 = 0
    guess_limit = 3
    while guess_3 != secret_alp_3 and not(out_of_guesses):
        if guess_count_3 < guess_limit:
            guess_3 = input("cro_odile : ")
            guess_count_3 += 1
        else:
            out_of_guesses = True
    if out_of_guesses:
        print("Out of guesses, YOU LOSE!")
    else:
        print("YOU WIN")
cond_1()