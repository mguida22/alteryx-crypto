# convert from pig_latin to english (as best is as possible)

import sys, json

VOWELS = 'aeiouAEIOU'
CONSONANT_CLUSTERS = ['bl', 'br', 'ch', 'cl', 'cr', 'dr', 'fl', 'fr', 'gl',
                      'gr', 'pl', 'pr', 'sc', 'sh', 'sk', 'sl', 'sm', 'sn',
                      'sp', 'st', 'sw', 'th', 'tr', 'tw', 'wh', 'wr', 'sch',
                      'scr', 'shr', 'sph', 'spl', 'spr', 'sq', 'str', 'thr']

def is_vowel(c):
    if c in VOWELS:
        return True
    return False

def is_consonant_cluster(s):
    for cluster in CONSONANT_CLUSTERS:
        if s == cluster:
            return True
    return False


def unpig(word):
    # IYAY, AYAY, OYAY
    if word[-3:] == 'YAY':
        return word[0]
    elif word[-3:] == 'yay':
        return word[:-3]
    elif word[-2:] == 'ay':
        word = word[:-2]

        if is_consonant_cluster(word[-3:]):
            return word[-3:] + word[:-3]
        elif is_consonant_cluster(word[-2:]):
            return word[-2:] + word[:-2]
        else:
            return word[-1:] + word[:-1]
    else:
        return word

if __name__ == '__main__':
    # print(unpig(sys.argv[1]))
    with open('new_text.txt', 'r') as f:
        data = f.read()

    out = []
    for word in data.split(' '):
        out.append(unpig(word))

    out = ' '.join(out)

    with open('out_text.txt', 'w') as f:
        f.write(out)
