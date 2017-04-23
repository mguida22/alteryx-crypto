# translate from english to pig_latin

def main():
   inputString = input("Please enter the text to be translated: ")
   print("Translated text:", translate(inputString))


def findFirstVowel(given_word):
   '''Returns the location of the first vowel in the given word.'''
   for i in range(len(given_word)):
       if checkVowel(given_word[i]) == True:
           return i


def translateWord(input_string):
   '''Translates the word and returns the translation to the caller.'''
   firstVowel = findFirstVowel(input_string)
   if firstVowel == None:
       translated = (input_string + "yay")
   elif firstVowel == 0:
       translated = (input_string + "yay")
   elif firstVowel >= 1:
       translated = (input_string[firstVowel:] +
                     input_string[:firstVowel] + "ay")
   else:
       pass
   return translated


def translate(inputWords):
   '''Accepts multiple words (separated by spaces) and will return the entire translated phrase.'''
   wordList = inputWords.split()
   translatedString = str()
   for word in range(len(wordList)):
       translatedString = (translatedString +
                           translateWord(wordList[word]) + " ")
   return translatedString


def checkVowel(char):
   '''Returns "True" if submitted charecter is a vowel.'''
   vowels = "AaEeIiOoUu"
   for vowel_test in vowels:
       if char == vowel_test:
           return True
   return False

if __name__ == '__main__':
   main()
