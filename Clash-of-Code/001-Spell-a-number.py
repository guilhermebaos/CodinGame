# Done on September 2021

digits = list(input())

dici = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
dicip = ['Zeros', 'Ones', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Sevens', 'Eights', 'Nines']
result = ''
skip_for = 0
for index, num in enumerate(digits):
    if skip_for > 0:
        skip_for -= 1
        continue
    times = 0
    for i, n in enumerate(digits[index + 1:]):
        if n == num:
            times += 1
        if n != num:
            break
    skip_for = times
    if times <= 0:
        result += dici[int(num)]
        result += ' '
    else:
        times += 1
        result += dici[int(times)]
        result += ' '
        result += dicip[int(num)]
        result += ' '
print(result[:-1])