#first define function to overturn the morse code language to letter
def overturn_morse_code(string, overturn_morse_dict):
# use slpit() function to split word in words 
    words = string.split(' ')
#loop through each word in words
    for word in words:
        letters = word.split(' ')
# a for loop to check every letter in the word
        for letter in letters:
# if letter in morse code language print the letter
            if letter in overturn_morse_dict.keys():
                print(overturn_morse_dict[letter])
# if letter is space a space is printed(space is used between each letter written)
            elif letter ==" ":
                print(" ")
# if letter is'/' then '/' is printed('/' is space between words)
            elif letter =="/":
                print("/")
# if the letter is not in the morse language then the code will print the key does not exist in our dictionary!
            else:
                print(f"The {letter}key doesn't exist in our dictionary!")
string = input("Enter morse code to print out into letters:")
# The overturn morse dictionary
overturn_morse_dict ={
    '.-': 'A',
    '-...': 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '--.': 'G',
    '....': 'H',
    '..': 'I',
    '.---': 'J',
    '-.-': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
    '--..--': ', ',
    '.-.-.-': '.',
    '..--..': '?',
    '-..-.': '/',
    '-....-': '-',
    '-.--.': '(',
    '-.--.-': ')',
    '-.-.--': '!'
}

#call the function to print the word 

overturn_morse_code(string, overturn_morse_dict)
