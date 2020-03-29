numbers = [1, 7, 9, 12, 13]
count_odd = 0
count_even = 0
for number in numbers:
    if number % 2 and number > 10:
        count_odd += 1
    else:
        count_even += 1
print(count_odd)
print(count_even)
