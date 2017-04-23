# generate pig_latin -> english dictionary

import json


def setup():
    word_set = set()
    to_english = {}
    with open("sonets.txt") as sonets:
        for line in sonets.readlines():
            line = line.split()
            for word in line:
                word = (word.strip()
                        .replace(".", "")
                        .replace("!", "")
                        .replace("?", "")
                        .replace(",", "")
                        .replace(":", "")
                        .replace(";", "")
                        .replace("-", "")
                        .replace("_", ""))

                if word not in word_set:
                    word_set.add(word)
                    converted_word = translateWord(word)
                    if not converted_word.islower():
                        converted_word = converted_word.title()
                    to_english[converted_word] = word

    with open("to_english.json", "w") as json_dump_file:
        print(json.dumps(to_english, indent=2), file=json_dump_file)


def translate(inputWords):
    '''Accepts multiple words (separated by spaces) and will return the entire translated phrase.'''
    wordList = inputWords.split()
    translatedString = str()
    for word in range(len(wordList)):
        translatedString = (translatedString +
                            translateWord(wordList[word]) + " ")
    return translatedString


if __name__ == '__main__':
    setup()
