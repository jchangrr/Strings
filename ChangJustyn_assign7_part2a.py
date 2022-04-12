"""
Assignment #7, Part 2a
Justyn Chang
"""
#import module
import random

#define function
def add_letters(word, num):
    newword = ""
    #build loop
    for i in word:
        newword = newword + i
        for i in range(num):
            new = ""
            #get random integers and convert to letters
            while True:
                rand = random.randint(65, 122)
                if rand >= 91 and rand <= 96:
                    rand = random.randint(65, 122)
                else:
                    letter = chr(rand)
                    new = new + letter
                    break
            #add letters to word
            newword = newword + new
    #return newword
    return newword

#define function
def remove_letters(word, num):
    newword = ""
    i = 0
    #build loop
    count = len(word)
    #remove letters as needed
    while i < count:
        newword = newword + word[i]
        i = i + (num + 1)
    #return newword
    return newword

#define function
def shift_characters(word, num):
    newword = ""
    #build loop
    for i in word:
        #change characters into ascii
        code = ord(i)
        #add one to ascii and convert back to characters
        newword = newword + chr(code + num)
    #return newword
    return newword

