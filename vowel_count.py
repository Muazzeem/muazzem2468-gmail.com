list = 'mamun,arif,asif'
count = 0
vowels = 'aeiou'
for letters in list:
    if letters in vowels:
        count += 1
print(count)
