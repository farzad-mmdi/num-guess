import random

def num_guess():
    while True:
        try:
            From = int(input('from:'))
            To = int(input('to:'))
            random_num = random.randint(From,To)
        except ValueError:
            print('wrong value') 
        else:
            break       
    
    while True:
            yours = input('guess the number:\nor enter --show to see the number:\n')
            try:
                Int = int(yours)
                if random_num == Int:
                    print('thats correct')
                    break
                else:
                    print('try again')
            except ValueError:
                Str = str(yours) 
                if Str == '--show':
                    print(random_num)
                    break
                else:
                    print('try again')


num_guess()            