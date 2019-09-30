import random
secretnumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')

for guessesTaken in range(1, 7):
    print('take a guess.')
    guess = int(input())

    if guess < secretnumber:
        print('Your guess is too low.')
    elif guess > secretnumber:
        print('Your guess is too high.')
    else:
        break

if guess == secretnumber:
    print("Good job!,You guessed my number in " + str(guessesTaken) + ' guessess!')           
else:
    print('Nope.The number I was thinking of was ' + str(secretnumber))



# def spam():
#     global eggs
#     eggs = 'spam'
#     print(eggs)
# eggs = 5    
# spam()
# print(eggs)    

# def divide(divideBy):
#     try:
#         return 42/ divideBy
#     except ZeroDivisionError:
#         print('Error:Invalid argument.')    
# print(divide(2))
# print(divide(12))
# print(divide(0))
# print(divide(1))   

# def divide1(divideBy):
#     return 42 / divideBy
# try:
#     print(divide1(2))
#     print(divide1(12))
#     print(divide1(0))
#     print(divide1(1))
# except ZeroDivisionError:
#      print('Error: Invalid argument.')