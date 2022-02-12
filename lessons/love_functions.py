"""Some examples of tender, loving function definitions."""


def love(Angela: str) -> str:  
    """Given a name as a parameter, returns a loving string."""
    return f"I love you {Angela}!"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loving message n times."""
    love_note: str = ""
    counter_variable: int = 0
    while counter_variable < n:
        love_note += love(to) + "\n"
        counter_variable += 1
    return love_note
