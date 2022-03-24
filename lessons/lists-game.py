"""Examples of using lists in a simple 'game'."""


def vowels(word: str) -> str:
    """Return."""
    i: int = 0
    vowels: list[str] = ["a", "e", "i", "o", "u"]
    final: str = ""
    while i < len(word):    
        for vowels[i] in word:
            final += vowels[i]
            i += 1
        if word[i] % 3 == 0:
            final += word[i]
            i += 1

    print(final)