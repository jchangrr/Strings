"""
Assignment #7, Part 1b
Justyn Chang
"""
#copy and paste code from part 1b
while True:
    user = input("Enter a username: ")

    length = len(user)
    print("* Length of username: ", length)

    alnum = user.isalnum()
    print("* All characters are alpha-numeric: ", alnum)

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

#build loop
while True:
    #ask for password
    password = input("Enter a password: ")

    #determine length of password
    plength = len(password)
    print("* Length of password: ", plength)

    #find if password is part of username
    count = password.count(user)
    if count == 0:
        part = False
    else:
        part = True
    print("* Username is part of password ", part)

    #find how many uppercase, lowercase, digits, and special characters are in password
    puppercase = 0
    plowercase = 0
    pdigits = 0
    special = 0
    for i in range(0, plength):
        if ord(password[i]) >= 65 and ord(password[i]) <= 90:
            puppercase += 1
        if ord(password[i]) >= 97 and ord(password[i]) <= 122:
            plowercase += 1
        if ord(password[i]) >= 48 and ord(password[i]) <= 57:
            pdigits += 1
        if ord(password[i]) >= 35 and ord(password[i]) <= 38:
            special += 1    
    print("* # of uppercase characters in the password: ", puppercase)
    print("* # of lowercase characters in the password: ", plowercase)
    print("* # of digits in the password: ", pdigits)
    print("* # of special characters in the password: ", special)

    #validate password
    if (plength >= 8) == False:
        print("Password is invalid, please try again")
        print()
    elif part == True:
        print("Password is invalid, please try again")
        print()
    elif puppercase == 0:
        print("Password is invalid, please try again")
        print()
    elif plowercase == 0:
        print("Password is invalid, please try again")
        print()
    elif pdigits == 0:
        print("Password is invalid, please try again")
        print()
    elif special == 0:
        print("Password is invalid, please try again")
        print()
    else:
        print("Password is valid!")
        print()
        break
