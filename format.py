# formatting for visual grepping of text

with open('small_data.txt', 'r') as f:
    data = f.read()

outdata = ''

for i in range(2, len(data) - 2, 2):
    # data = data[:i] + '_' + data[i:]
    outdata += data[i-2] + data[i-1] + '_'

with open('small_data.txt', 'w') as out:
    out.write(outdata)
