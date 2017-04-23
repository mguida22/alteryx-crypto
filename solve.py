import string

with open('full_data.txt', 'r') as f:
    data = f.read()

lookup = {
    'qs': 'y',
    'qS': 'Y',
    'ad': ' ',
    'ac': 'a',
    'aC': 'A',
    '5c': 'e',
    '5C': 'E',
    '7s': 't',
    '7S': 'T',
    '2s': 'o',
    '2S': 'O',
    '6s': 's',
    '6S': 'S',
    '8c': 'h',
    '8C': 'H',
    '9c': 'i',
    '9C': 'I',
    'as': 'n',
    'aS': 'N',
    '5s': 'r',
    '5S': 'R',
    'qc': 'l',
    'qC': 'L',
    '4c': 'd',
    '4C': 'D',
    '8s': 'u',
    '8S': 'U',
    'kh': '\n',
    'ts': 'w',
    'tS': 'W',
    'kc': 'm',
    'kC': 'M',
    '6c': 'f',
    '6C': 'F',
    '3d': ',',
    '3D': ',',
    '3c': 'c',
    '3C': 'C',
    '7c': 'g',
    '7C': 'G',
    '2c': 'b',
    '2C': 'B',
    '3s': 'p',
    '3S': 'P',
    '9s': 'v',
    '9S': 'V',
    'jh': '\'',
    'jc': 'k',
    'jC': 'K',
    '2d': '.',
    '2D': '.',
    '5d': ':',
    'td': '-',
    '2h': '1',
    '4d': '?',
    '4s': 'q',
    '4S': 'Q',
    'tc': 'j',
    'tC': 'J',
    'th': '9',
    '6d': ';',
    'js': 'x',
    'jS': 'X',
    '8d': '(',
    '9d': ')',
    'ah': '0',
    'ks': 'z',
    'kS': 'Z',
    '3h': '2',
    '7h': '6',
    '4h': '3',
    '6h': '5',
    '8h': '7',
    '5h': '4',
    '9h': '8',
}

data = list(data)
SIZE = 2
new_data = []
for i in range(0, len(data) - SIZE, SIZE):
    match = data[i:i+SIZE]
    match = ''.join(match)
    try:
        replace = lookup[match]
    except:
        # replace = '[{}]'.format(match)
        replace = '-'

    new_data.append(replace)

new_data = ''.join(new_data)

with open('new_text_full.txt', 'w') as f:
    f.write(new_data)
