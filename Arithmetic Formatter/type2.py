txt = ["321 + 89", "56 - 413", "329 + 67", "523 - 49", "45 + 525"]
new_txt = []
for i in txt:
    new_txt += i.split(',')

print(new_txt)

