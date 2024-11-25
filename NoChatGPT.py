""" required only once
list = []
with open("words.txt","r") as f:
    for line in f:
        word = line.strip()
        if word.isalpha() and len(word)==5:
            list.append(word.lower())

with open("words.txt","w") as f:
    for word in list:
        f.write(word+"\n")
"""
import random

liste = []
with open("words.txt","r") as f:
    for line in f:
        liste.append(line[:-1:])

correct_word = random.choice(liste)
correct_word_list = list(correct_word)
#Let start the game

print(""" W   W  OOO  RRRR   DDDD   L      EEEE
 W   W O   O R   R  D   D  L      E
 W W W O   O RRRR   D   D  L      EEE
 WW WW O   O R  R   D   D  L      E
 W   W  OOO  R   R  DDDD   LLLLL  EEEE
""")
print(correct_word_list)
print("Guess the word in 5 Chances")
n = 1
while True:
    if n > 5:
        break
    guess = input("Enter the word: ").lower()
    if guess == correct_word:
        print("Correct!")
        break
    elif guess.isalpha() and len(guess)==5 and guess in liste:
        n=n+1
        for i in range(5):
            if guess[i] == correct_word_list[i]:
                print(guess[i],end="")
            else:
                print("*",end="")
        print("")
    else:
        print("Iski coding tera baap karega")



