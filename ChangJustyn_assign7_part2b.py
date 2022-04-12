"""
Assignment #7, Part 2b
Justyn Chang
"""
#copy and paste codes from part 2a
import random
def add_letters(word, num):
    newword = ""
    for i in word:
        newword = newword + i
        for i in range(num):
            new = ""
            while True:
                rand = random.randint(65, 122)
                if rand >= 91 and rand <= 96:
                    rand = random.randint(65, 122)
                else:
                    letter = chr(rand)
                    new = new + letter
                    break
            newword = newword + new
    return newword

def remove_letters(word, num):
    newword = ""
    i = 0
    count = len(word)
    while i < count:
        newword = newword + word[i]
        i = i + (num + 1)
    return newword

def shift_characters(word, num):
    newword = ""
    for i in word:
        code = ord(i)
        newword = newword + chr(code + num)
    return newword

#build loop
while True:
    #ask for action
    action = input("(e)ncode, (d)ecode or (q)uit: ")
    #if "e", then ask for number and phrase, and then add letters and shift
    if action == "e":
        num = int(input("Enter a number between 1 and 5: "))
        while (num >= 1 and num <= 5) == False:
            num = int(input("Enter a number between 1 and 5: "))
        encode = input("Enter a phrase to encode: ")
        print("Your encoded word is: ", shift_characters(add_letters(encode, num), num))
    #if "d", then ask for number and phrase, and then remove letters and shift
    elif action == "d":
        num = int(input("Enter a number between 1 and 5: "))
        while (num >= 1 and num <= 5) == False:
            num = int(input("Enter a number between 1 and 5: "))
        decode = input("Enter a phrase to decode: ")
        print("Your decoded word is: ", shift_characters(remove_letters(decode, num), (num * -1)))
    #if "q", then quit program
    elif action == "q":
        break

