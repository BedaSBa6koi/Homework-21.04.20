enter = input('Enter text ')
enter = enter.replace(' ', '')

small = 0
big = 0
length = len(enter)

for i in enter:
    if i.islower():
        small += 1
    elif i.isupper():
        big +=1


per_small = small / length * 100
per_big = big / length * 100

print(f'Small letters: {per_small:.2f}%')
print(f'Capital letters: {per_big:.2f}%')