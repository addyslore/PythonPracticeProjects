txt = ["321 + 89", "56 - 413", "329 + 67", "49 - 234", "45 + 55"]

new_txt = []
for i in txt:
    a = i.replace(' ', '')
    new_txt.append(a)

print(new_txt)

first_line = ''
second_line = ''
mid_line = ''
third_line = ''

for i in new_txt:
    if '+' in i:
        a = i.split('+')
        l = len(a[0])
        h = max(len(a[0]), len(a[1])) + 2
        first_line += ' ' * (h - l) + a[0] + '    '
        ll = len(a[1])
        second_line += '+ ' + ' ' * (h - ll - 2) + a[1] + '    '
        mid_line += '-' * h + '    '
        third_line += ' ' * (h - len(str(int(a[0]) + int(a[1])))) + str(int(a[0]) + int(a[1])) + '    '
    elif '-' in i:
        b = i.split('-')
        l = len(b[0])
        h = max(len(b[0]), len(b[1])) + 2
        first_line += ' ' * (h - l) + b[0] + '    '
        ll = len(b[1])
        second_line += '- ' + ' ' * (h - ll - 2) + b[1] + '    '
        mid_line += '-' * h + '    '
        third_line += ' ' * (h - len(str(int(b[0]) - int(b[1])))) + str(int(b[0]) - int(b[1])) + '    '
    else:
        print('Error: Operator must be "+" or "-".')

print(first_line.rstrip())
print(second_line.rstrip())
print(mid_line.rstrip())
print(third_line.rstrip())