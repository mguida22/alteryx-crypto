# pig to english from dictionary

import json

with open("to_english.json") as to_english:
    to_english = json.loads(to_english.read())

with open("short_text.txt") as short_text:
    short_text = short_text.read()


for key, value in to_english.items():
    short_text = short_text.replace(key, value)

with open("short_translated.txt", "w") as short_translated:
    print(short_text, file=short_translated)
