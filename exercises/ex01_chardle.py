"""Chardle. My first game."""

__author__ = "730391695"


entered_word: str = input("Enter a 5-character word ")
if len(entered_word) != 5:
    print("Error: Word must contain 5 characters. ")
    exit("Try again. ")
entered_letter: str = input("Enter a single character ")
if len(entered_letter) != 1:
    print("Error: Character must be a single character. ")
    exit("Try again. Input a single character next time.")
print("Searching for " + entered_letter + " in " + entered_word)

times_appeared: int = 0
if entered_letter == entered_word[0]:
    print(entered_letter + " found at index 0 ")
    times_appeared = times_appeared + 1
if entered_letter == entered_word[1]:
    print(entered_letter + " found at index 1 ")
    times_appeared = times_appeared + 1
if entered_letter == entered_word[2]:
    print(entered_letter + " found at index 2")
    times_appeared = times_appeared + 1
if entered_letter == entered_word[3]:
    print(entered_letter + " found at index 3 ")
    times_appeared = times_appeared + 1
if entered_letter == entered_word[4]:
    print(entered_letter + " found at index 4 ")
    times_appeared = times_appeared + 1

if times_appeared == 0:
    print("No instances of " + entered_letter + " found in " + entered_word)
else:
    if times_appeared == 1:
        print(str(times_appeared) + " instance of " + entered_letter + " found in " + entered_word)
    else:
        print(str(times_appeared) + " instances of " + entered_letter + " found in " + entered_word)

                    