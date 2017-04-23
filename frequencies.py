import string

with open('full_data.txt', 'r') as f:
    data = f.read()


# Generate frequencies of characters in data

SIZE = 2
d = {}
for i in range(0, len(data) - SIZE, SIZE):
    match = data[i:i+SIZE]
    match = match.lower()
    if match in d:
        d[match] = d[match] + 1
    else:
        d[match] = 1


s = [(k, d[k]) for k in sorted(d, key=d.get, reverse=True)]

total = 0
for k, v in s:
    total += v

i = 0
for k, v in s:
    # print(i)
    print(k, (v / total) * 100)
    i += 1

freq = []
for k, v in s:
    freq.append(k)

print(freq)
