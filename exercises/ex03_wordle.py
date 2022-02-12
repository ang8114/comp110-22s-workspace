"""Structured Wordle."""

__author__ = "730391695"


def contains_char(entered_word: str, searched_character: str) -> bool:
    """Returns bool when searched for a character."""
    assert len(searched_character) == 1
    i: int = 0
    while i < len(entered_word):
        if searched_character == entered_word[i]:
            return True  
        else:    
            i = i + 1
    return False


def emojified(guessed_word: str, secret_word: str) -> str:
    """Returns a string of emoji boxes that indicate right or wrong."""
    assert len(guessed_word) == len(secret_word)
    emoji_boxes: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"  
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == guessed_word[i]:
            emoji_boxes = emoji_boxes + GREEN_BOX
        else:
            alt_index: int = 0
            guessed_character: bool = False
            while alt_index < len(guessed_word):
                if contains_char(secret_word, guessed_word[i]):
                    guessed_character = True
                alt_index = alt_index + 1
            if guessed_character is True:
                emoji_boxes = emoji_boxes + YELLOW_BOX
            else:
                emoji_boxes = emoji_boxes + WHITE_BOX
        i = i + 1
    return emoji_boxes


def input_guess(expected_len: int) -> str:
    """Prompts for a guess word of the correct length."""
    entered_word: str = input("Enter a " + str(expected_len) + " character word: ")
    while len(entered_word) != expected_len:
        entered_word = input("That wasn't " + str(expected_len) + " chars! Try again: ")
    return entered_word
            

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns_left: int = 1
    entered_word = ""
    guessed_word: bool = False
    while not guessed_word and turns_left <= 6:
        print("=== Turn " + (str(turns_left)) + "/6 turns ===")
        entered_word = input_guess(5)
        print(emojified(entered_word, secret_word))
        turns_left += 1
        if entered_word == secret_word and turns_left <= 6:
            print(f"You won in {str(int(turns_left - 1))}/6 turns!")
            guessed_word = True
    if entered_word != secret_word and turns_left > 6:
        print("X/6 - Sorry, try again tomorrow!")

  
if __name__ == "__main__":
    main()