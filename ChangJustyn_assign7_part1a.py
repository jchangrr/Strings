"""
Assignment #7, Part 1a
Justyn Chang
"""
#build loop
while True:
    #ask for username
    user = input("Enter a username: ")

    #find length of username
    length = len(user)
    print("* Length of username: ", length)

    #determine if all characters are alpha-numeric
    alnum = user.isalnum()
    print("* All characters are alpha-numeric: ", alnum)

    #find if first and last characters are digits
    first = user[0]
    if ord(first) >= 48 and ord(first) <= 57:
        firstdig = False
    else:
        firstdig = True
    last = user[-1]
    if ord(last) >= 48 and ord(last) <= 57:
        lastdig = False
    else:
        lastdig = True
    if firstdig == True and lastdig == True:
        firstlast = True
    else:
        firstlast = False
    print("* First & last characters are not digits: ", firstlast)

    #determine how many lowercase, uppercase, and digits are in the username
    uppercase = 0
    lowercase = 0
    digits = 0
    for i in range(0, length):
        if ord(user[i]) >= 65 and ord(user[i]) <= 90:
            uppercase += 1
        if ord(user[i]) >= 97 and ord(user[i]) <= 122:
            lowercase += 1
        if ord(user[i]) >= 48 and ord(user[i]) <= 57:
            digits += 1
    print("* # of uppercase characters in the username: ", uppercase)
    print("* # of lowercase characters in the username: ", lowercase)
    print("* # of digits in the username: ", digits)

    #validate the username
    if (length >= 8 and length <= 15) == False:
        print("Username is invalid, please try again")
        print()
    elif alnum == False:
        print("Username is invalid, please try again")
        print()
    elif firstlast == False:
        print("Username is invalid, please try again")
        print()
    elif uppercase == 0:
        print("Username is invalid, please try again")
        print()
    elif lowercase == 0:
        print("Username is invalid, please try again")
        print()
    elif digits == 0:
        print("Username is invalid, please try again")
        print()
    else:
        print("Username is valid!")
        print()
        break
