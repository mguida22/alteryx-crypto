# used to generate all collisions in the final text

import json


def findFirstVowel(given_word):
    '''Returns the location of the first vowel in the given word.'''
    for i in range(len(given_word)):
        if checkVowel(given_word[i]) == True:
            return i


def checkVowel(char):
    '''Returns "True" if submitted charecter is a vowel.'''
    vowels = "AaEeIiOoUuyY"
    for vowel_test in vowels:
        if char == vowel_test:
            return True
    return False


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


with open("final_proof.txt") as final_proof:
    final_proof = final_proof.read()
    final_proof_words = final_proof.split()

word_dict = {}


for word in final_proof_words:
    word = (word.strip()
            .replace(".", "")
            .replace("!", "")
            .replace("?", "")
            .replace(",", "")
            .replace(":", "")
            .replace(";", "")
            .replace("-", "")
            .replace("_", "")
            # .replace("'", "")
            .replace("\"", "")).lower()
    pig_word = translateWord(word).lower()

    if pig_word in word_dict.keys() and word not in word_dict[pig_word]:
        word_dict[pig_word].append(word)
    elif pig_word not in word_dict.keys():
        word_dict[pig_word] = [word]

duplicates = 0
duplicates_dict = {}
for key, val in word_dict.items():
    if len(val) >= 2:
        print("{0} == {1}".format(key, val))
        duplicates_dict[key] = val
        duplicates += 1

# print(json.dumps(duplicates_dict, indent=2))
pretty_print = "{\n"
for item in duplicates_dict:
    pretty_print += "  \"{}\": [\"{}\", \"{}\"],\n".format(item, duplicates_dict[item][0], duplicates_dict[item][1])
pretty_print += "}"
with open('collisions.json', 'w') as f:
    # print(json.dumps(duplicates_dict, indent=2), file=f)
    f.write(pretty_print)
