# Used to help iterate through potential coded pairs to character mappings

import operator
import json
import re

with open("values.json") as values:
    json_values = json.loads(values.read())

with open("Alteryx_CUHack2017.txt") as file:
    file = file.read()

with open("words.json") as top_1000_words:
    top_1000_words = json.loads(top_1000_words.read())
    for i in range(len(top_1000_words)):
        top_1000_words[i] = top_1000_words[i].lower()

file = re.findall("..", file)

lenth = 0

new_list = []

for item in file:
    if item.lower() == "ad":
        new_list.append(" ")
    else:
        new_list.append(item)


joined = "".join(new_list)
space_split = joined.split()
most_common = {}

for item in space_split:

    if item in most_common:
        most_common[item][0] += 1
    else:
        most_common[item] = [1]

for key, value in most_common.items():
    broken_out = re.findall("..", key)
    parsed_out = []

    for item in broken_out:
        if item.lower() in json_values.keys():
            parsed_out.append(json_values[item.lower()])
        else:
            parsed_out.append(item)

    most_common[key].append(parsed_out)


sorted_x = sorted(most_common.items(),
                  key=operator.itemgetter(1), reverse=True)[:-20]

count = 0
finished_words = []
for item in sorted_x:
    count += 1
    word = ""
    if item[0][-6:].lower() == "qsacqs":  # if ends in 'yay'
        for letter in item[1][1]:
            if len(letter) == 1:
                word += letter
            else:
                word += "-"

        word = word[:-3]

        if "-" not in word:
            finished_words.append(word)
        else:
            print("error on '{0}'".format(word))

    elif item[0][-4:].lower() == "acqs":  # if ends in 'ay'
        for letter in item[1][1]:
            if len(letter) == 1:
                word += letter
            else:
                word += "-"
        word = word[:-2]

    print("{0:<20} {1:<7} {2}".format(item[0], word, item[1][1]))

    if count > 50:
        break

for word in finished_words:
    if word.lower() not in top_1000_words:
        print("didn't find '{0}'".format(word))

print(len(sorted_x))
