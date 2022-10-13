import random
suma = []
numbers = []
def split():
    first_guess = True
    suma.clear()
    while len(suma) != 4:
        if not first_guess:
            print("Invalid number")
            suma.clear()
        guess = int(input('Give me a number: '))
        while guess > 0:
            guess, digit = divmod(guess, 10)
            suma.append(digit)
        first_guess = False
    return list(reversed(suma))


def rand():
    for i in range(1, 5):
        numbers.append(random.randint(1,9))
    return numbers

if __name__ == '__main__':
    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    rand(), split()
    cows = 0
    bulls = 0
    guesses = 0
    while suma != numbers:
        cows = 0
        bulls = 0
        for x in range(len(suma)):
            if suma[x] == numbers[x]:
                cows += 1
                guesses += 1
            else:
                bulls += 1
                guesses += 1
        print(f'{cows} cows, {bulls} bulls')
        split()
    print(f'Congratulations! You passed the test after {guesses/4:.0f} attempts!')
