import random

print("PERMAINAN TEBAK ANGKA")

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f"Masukkan angka tebakan mu antara 1 & {x}: "))
        if guess < random_number:
            print("Salah coba lagi, angka tebakan mu terlalu kecil")
        elif guess > random_number:
            print("Salah coba lagi, angka tebakan mu terlalu besar")

    print(f"yeiii... selamat, tebakan mu {random_number} benar ")

guess(20)