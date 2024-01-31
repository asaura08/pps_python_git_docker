import random

def frotar(n_frases: int = 1) -> list:
    return random.choices(open("frases.txt").read().splitlines(), k=n_frases)
