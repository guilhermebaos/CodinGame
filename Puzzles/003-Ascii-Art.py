l = int(input())
h = int(input())
t = list(input())
letters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ?')
ascii_letters = [[[] for _ in range(h)] for _ in range(len(letters))]
y = 0
for i in range(h):
    row = list(input())
    for char in range(len(letters)):
        ascii_letters[char][y] = ''.join(row[l * char:l * (char + 1)])
    y += 1

result = ['' for _ in range(h)]
for char in t:
    try:
        ascii_char = ascii_letters[letters.index(char.upper())]
    except ValueError:
        ascii_char = ascii_letters[letters.index('?')]
    for index, line in enumerate(ascii_char):
        result[index] += line

for line in result:
    print(''.join(line))
