import random

print("Welcome to Gucci: Your Number Guessing App")

attempts = 5
rand_num = random.randint(0, 10)

for x in range(attempts):
    number = int(input("What number am I thinking?\nMy number is between 0 and 10: "))
    if number == rand_num:
        print(f"Congratulations, your guess is correct. The number is: {rand_num}")
        break
    else:
        remaining = attempts - x - 1
        print(f"Wrong guess. You have {remaining} attempts left.")
        if remaining == 0:
            print(f"Game Over!!! The number is: {rand_num}")
