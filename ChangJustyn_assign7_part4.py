"""
Assignment #7, Part 4
Justyn Chang
"""
#define function
def string_length(word):
    #make counter
    count = 0
    #create loop
    for i in word:
        count += 1
    #return count
    return count

#define function
def string_isalpha(word):
    #make counter
    count = 0
    #set variable to false
    alpha = False
    #set loop with conditions for making variable false or true
    for i in word:
        if (ord(word[count]) >= 65 and ord(word[count]) <= 90) or (ord(word[count]) >= 97 and ord(word[count]) <= 122):
            alpha = True
        else:
            alpha = False
            break
        count += 1
    #return alpha
    return alpha

#define function
def string_isupper(word):
    #make counter
    count = 0
    #set variable to false
    upper = False
    #set loop with conditions for making variable false or true
    for i in word:
        if (ord(word[count]) >= 65 and ord(word[count]) <= 90):
            upper = True
        else:
            upper = False
            break
        count += 1
    #return upper
    return upper

#define function
def string_isdigit(word):
    #make counter
    count = 0
    #set variable to false
    digit = False
    #set loop with conditions for making variable false or true
    for i in word:
        if (ord(word[count]) >= 48 and ord(word[count]) <= 57):
            digit = True
        else:
            digit = False
            break
        count += 1
    #return digit
    return digit

#define function
def string_swapcase(word):
    #make counter
    count = 0
    #evaluate word for lowercase and uppercase, and swap them
    newword = ""
    word1 = word
    for i in word:
        if (ord(word[count]) >= 65 and ord(word[count]) <= 90):
            new = chr(ord(word[count]) + 32)
        elif (ord(word[count]) >= 97 and ord(word[count]) <= 122):
            new = chr(ord(word[count]) - 32)
        elif (ord(word[count]) >= 48 and ord(word[count]) <= 57) or ord(word[count]) == 32:
            new = chr(ord(word[count]))
        newword = newword + new
        count += 1
    #return newword
    return newword

#define function
def string_lower(word):
    #make counter
    count = 0
    #evaluate word for lowercase and uppercase, and change uppercase to lowercase
    newword = ""
    word1 = word
    for i in word:
        if (ord(word[count]) >= 65 and ord(word[count]) <= 90):
            new = chr(ord(word[count]) + 32)
        elif (ord(word[count]) >= 97 and ord(word[count]) <= 122):
            new = chr(ord(word[count]))
        elif (ord(word[count]) >= 48 and ord(word[count]) <= 57) or ord(word[count]) == 32:
            new = chr(ord(word[count]))
        newword = newword + new
        count += 1
    #return newword
    return newword
