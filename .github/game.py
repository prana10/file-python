#game tebak angka bareng bot

import random

print("halo halo")
print("ini adalah game tebak angka")
print("hanya ada 3 kesempatan")
print("game ini dibuat oleh prana dhika")
print("referensi berasal dari python hub")
num = 3
print(num,"guesses left")
print("tebak angka diantara 1 sampai 10")
while True:
    guess = input()
    computer = random.randint(1, 10)
    print("tebakan mu: ",guess)
    print("tebakan computer: ",computer)
    print()
    if 0<int(guess)<11 and (int(guess) == computer):
        print("hore!! anda menang")
        break
    elif num == 1:
        print("tidak ada tebakan\nanda kalah")
        break
    else:
        print("sorry tebak lagi")
        num -= 1
    print(num,"guesses left")
    print("guess the number between 1 to 10")




