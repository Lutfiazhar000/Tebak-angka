import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else: 
            guess = low 
        feedback = input(f"apakah angka tebakan komputer {guess} terlalu besar (H), terlalu kecil (L) atau benar (C)?? ".lower())
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = +1

    print(f"yay! komputer berhasil menebak angka mu ({guess}) dengan tepat")

computer_guess(100)