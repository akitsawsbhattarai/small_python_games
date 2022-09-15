import random

print("guess the number between: " )
lowrange = int(input (f"(lowvalue): "))
highrange = int(input(f"and (highvalue): "))

result = ""
attempt = 0
while result != "c":
    attempt += 1
    if lowrange != highrange:
        guessed_number = random.randint(lowrange, highrange)
        result = input(f" Is {guessed_number} too high (H), too low (L) or correct (C) ? => ").lower()

        if result == "h":
            highrange = guessed_number - 1
        elif result == "l":
            lowrange =  guessed_number + 1
    else:
        guessed_number = lowrange

print(f" yay!! computer guessed {guessed_number} correctly in {attempt} attempt!")