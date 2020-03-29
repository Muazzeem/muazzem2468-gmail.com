list = 'mamun,saiful,asif'
count = 0
consonent = 'bcdfghijklmnpqustvzxyz'
for letters in list:
    if letters in consonent:
        count += 1
print(count)
