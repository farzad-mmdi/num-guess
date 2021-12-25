import random

def num_guess():
    From = int(input('from:'))
    To = int(input('to:'))
    random_num = random.randint(From,To)
    print(random_num)
    while True:
        yours = input('guess the number:')
        if random_num == int(yours):
            print('thats correct')
            break
        else:
            print('try again') 


num_guess()            