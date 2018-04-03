import math
def guess():
    A, B = map(int, input('enter the lower bound and upper bound respectively of your number\n').split(" "))
    N = int(input('number of guesses in which you wanted to guess your number\n'))
    i = 1
    while i <= N:
        d = math.ceil((A + B)/2)
        print('is your number is this',d)
        ans = str(input('enter your choice as TOO_BIG, TOO_SMALL or CORRECT\n'))
        if ans == 'TOO_SMALL':
            A = int(d)
        elif ans == 'TOO_BIG':
            B = int(d)
        elif ans == 'CORRECT':
            break
        else:
            print('WRONG_ANSWER, please do it again')
            break
        i = i + 1
    print('perhaps, we are not able to get the correct number in this limited number of gusses but still we has narrowed you range\n your number lies between',A, B)

guess()
