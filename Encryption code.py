# define the a function to encrypt letters,numbers and punctiation to morse code language
def morse_it(string, morse_dict):
# upper() is used to uppercase all letters written in the user's input
    string = string.upper()
# iterate through each character in the input string 
    for letter in string:
# if the letter written is in the dictionary then its corresponding morse code will be printed
        if letter in morse_dict.keys():
            print(morse_dict[letter])
#if the letter written is space, a space will be printed 
        elif letter ==" ":
            print(" ")
#if the letter is not in the dictionary , an error message will be printed
        else:
            print(f"The{letter}key doesn't exist in our dictionary!")
#prompt the user to enter a string
string = input("Enter somthing to print out to morse code:")
# create a dictionary cointaning the morse code for each character
morse_dict = { 
  #letters
  'A':'.-', 
  'B':'-...', 
  'C':'-.-.', 
  'D':'-..', 
  'E':'.', 
  'F':'..-.', 
  'G':'--.', 
  'H':'....', 
  'I':'..', 
  'J':'.---', 
  'K':'-.-', 
  'L':'.-..', 
  'M':'--', 
  'N':'-.', 
  'O':'---', 
  'P':'.--.', 
  'Q':'--.-', 
  'R':'.-.', 
  'S':'...', 
  'T':'-', 
  'U':'..-', 
  'V':'...-', 
  'W':'.--', 
  'X':'-..-', 
  'Y':'-.--', 
  'Z':'--..', 
  #numbers
  '1':'.----', 
  '2':'..---', 
  '3':'...--', 
  '4':'....-', 
  '5':'.....', 
  '6':'-....', 
  '7':'--...', 
  '8':'---..', 
  '9':'----.', 
  '0':'-----', 
  #punctuation and symbols
  ', ':'--..--', 
  '.':'.-.-.-', 
  '?':'..--..', 
  '/':'-..-.', 
  '-':'-....-', 
  '(':'-.--.', 
  ')':'-.--.-',
  '!':'-.-.--'
  }

# call the function to print the word in morse launguage
morse_it(string, morse_dict)
