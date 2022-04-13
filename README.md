# Strings
Part 1a:
You have been asked to write a username validation program for a small website. The website has specific rules on what constitutes a valid username, including:

All usernames must be between 8 and 15 characters long
Usernames can only contain alphabetic (a-z and A-Z) and numeric characters (0-9) - no special characters or spaces are allowed.
The first and last characters in a username cannot be a digit
Usernames must contain at least one uppercase character
Usernames must contain at least one lowercase character
Usernames must contain at least one numeric character
Write a program that asks the user to enter in a username and then examines that username to make sure it complies with the rules above. 

Part 1b:
The company you are working for was very happy with your username validator, and now they want you to write a password manager for their website. Here are the rules for passwords:

Passwords must be at least 8 characters long (but they do not have an upper limit)
Passwords cannot contain the user's username (i.e. if the username is "My1stUsername" the password cannot be "abcMy1stUsername" or "My1stUsernameABC" because the username String can be found in the password String)
Passwords must be a mixture of uppercase letters (A-Z), lowercase letters (a-z), digits (0-9) and a select number of special characters (#, $, % and &). The password must contain at least one of each of these types of characters in order to be valid.

Part 2a:
For this part you will be writing a series of functions that can be used as part of a "secret message encoder" program. Here are the functions you will be writing.

 function:   add_letters
 input:      a word to scramble (String) and a number of letters (integer)
 processing: adds a number of random letters (A-Z; a-z) after each letter 
             in the supplied word. for example, if word="cat" and num=1 
             we could generate any of the following:
             cZaQtR
             cwaRts
             cEaett
 
             if word="cat" and num=2 we could generate any of the following:
             cRtaHFtui
             cnnaNYtjn
             czAaAitym

output:     returns the newly generated word

 function:   remove_letters
 input:      a word to unscramble (String) and the number of characters to remove (integer)
 processing: the function starts at the first position in the supplied word and keeps it.
             it then removes "num" characters from the word. the process is repeated again
             if the word contains additional characters - the next character is kept
             and "num" more characters are removed.  For example, if word="cZaYtU" and
             num=1 the function will generate the following:
        
             cat (keeping character 0, removing character 1, keeping character 2, removing
                  character 3, keeping character 4, removing character 5)

 output:     returns the newly unscrambed word
 
 function:   shift_characters
 input:      a word (String) and a number of characters to shift (integer)
 processing: shifts each character in the supplied word to another position in the ASCII
             table. the new position is dictated by the supplied integer.  for example,
             if word = "apple" and num=1 the newly generated word would be:

             bqqmf

             because we added +1 to each character. if we were to call the function with
             word = "bqqmf" and num=-1 the newly generated word would be:
           
             apple

             because we added -1 to each character, which shifted each character down by
             one position on the ASCII table.

 output:     returns the newly generated word
 
 Part 2b:
 Now you are going to write an "encoder / decoder" program that makes use of your three cryptographic functions. Begin by writing a program that continually asks the user to enter in an option - the user can either (e)ncode a word, (d)ecode a word or (q)uit the program.

If the user chooses to encode a word you should do the following:

Ask the user for a positive number between 1 and 5. Reprompt them if necessary.
Next, ask them to enter in a phrase that they want to encode.
Finally, apply the following algorithm to their word:
Add 'num' random characters in between each letter of their word (using your add_letters) function
Shift the word 'num' characters (using your shift_characters function)
If the user chooses to decode a word you should do the following:

Ask the user for a positive number between 1 and 5. Reprompt them if necessary.
Next, ask them to enter in a phrase that they want to encode.
Finally, apply the following algorithm to their word:
Subtract 'num' random characters in between each letter of their word (using your remove_letters) function
Shift the word DOWN by 'num' characters (using your shift_characters function)

Part 3:
For this assignment you are going to write your own deterministic random number generator by using the 'middle square' algorithm. Here's how it works:

Begin with a six digit positive integer. We will call this our "seed" number.
Compute the square of the seed number.
Next, extract the six digits in the middle of the seed number.
The middle six digits will be a positive integer between 000000 and 999999. Compute the percentage of this number by dividing it by 999999
You now have a percentage value (i.e. 0.2467). We now need to covert this into a random number in a range that we want (i.e. integers between 3 and 10). This can be done by determining the difference between the low and the high value (i.e. 10 - 3 = 7) and multiplying the percentage by this difference (i.e. 0.2467 * 7). Then add in your start value (i.e. 0.2467 * 7 + 3) - convert the final number to an integer and you're done!
Start off by writing a simple program that performs this algorithm one time. Ensure that the user's input is validated accordingly (i.e. the seed value must be six characters long and must be all digits - use your string testing methods to do this!). Also ensure that the starting value is numeric and that it is smaller than your ending value. 

Once you are OK with the basic process you can move onto the next step of the program, which is to repeat the process a certain # of times to generate that many pseudorandom integers. Here's how this will work:

Begin by asking the user for a seed value, a low number and a high number (as above)
Also ask them for how many random integers they want to generate (a positive number >= 1)
Execute the process above to generate the first random number. At the end of the process you will need a new 'seed' - otherwise the next random number will be the same as the last one! You can do this by using the middle six digits of your previous 'seed' as the next 'seed' for your next random number generator.

Part 4:
For this part you will be implementing a series of commonly used String functions and methods by writing your own functions. These functions should behave just like their commonly used counterparts - here are some IPO notation blocks & sample code to get you started:

 function:   string_length
 input:      a word (String)
 processing: computes the length of the supplied String (without using the len() function)
 output:     returns the length of the string (integer)

 function:   string_isalpha
 input:      a word (String)
 processing: determines if the supplied String contains all alphabetic characters (A-Z,a-z)
             DO NOT USE THE "isalpha()" METHOD or any other String methods!
 output:     returns True of False (boolean)

 function:   string_isupper
 input:      a word (String)
 processing: determines if the supplied String contains all uppercase characters (A-Z)
             DO NOT USE THE "isupper()" METHOD or any other String methods!
 output:     returns True of False (boolean)

 function:   string_isdigit
 input:      a word (String)
 processing: determines if the supplied String contains all numeric characters (0-9)
             DO NOT USE THE "isdigit()" METHOD or any other String methods!
 output:     returns True of False (boolean)

 function:   string_swapcase
 input:      a word (String)
 processing: swaps uppercase characters with lowercase characters & vice-versa
             DO NOT USE THE "swapcase()" METHOD or any other String methods!
 output:     returns a new copy of the String

 function:   string_lower
 input:      a word (String)
 processing: converts all characters in a String to their lowecase equivalents
             DO NOT USE THE "lower()" METHOD OR "str.lower()"! or any other String methods!
 output:     returns a new copy of the String  
