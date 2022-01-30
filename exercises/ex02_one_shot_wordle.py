"""One Shot Wordle."""

__author__ = "730391691" 


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word = "python"
entered_word: str = input("What is your 6-letter guess? ")
i: int = 0
emoji_boxes: str = ""
entered_guess: int = 1
guessed_character: bool = False
alternate_i: int = 0

while len(entered_word) != len(secret_word):
    entered_word = input("That was not 6 letters! Try again: ")
while i < len(secret_word):
    alternate_i = 0
    if secret_word[i] == entered_word[i]:
        emoji_boxes = emoji_boxes + GREEN_BOX
    else:
        while guessed_character is False and alternate_i < len(secret_word):
            if secret_word[alternate_i] == entered_word[i]:
                guessed_character = True
            else:
                alternate_i = alternate_i + 1
        if guessed_character is True:
            emoji_boxes = emoji_boxes + YELLOW_BOX
            guessed_character = False
        else:
            emoji_boxes = emoji_boxes + WHITE_BOX
    i = i + 1
print(emoji_boxes)
if secret_word == entered_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
    
