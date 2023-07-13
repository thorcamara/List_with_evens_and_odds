numbers = [[], []]
values = 0
for c in range(1, 8):
    values = int(input(f'Type the {c}o number: '))
    if values % 2 == 0:
        numbers[0].append(values)
    else:
        numbers[1].append(values)
print('-=' * 30)
numbers[0].sort()
numbers[1].sort()
print(f'The \033[1;34mEVEN\033[m numbers are: \033[1;32m{numbers[0]}\033[m')
print(f'The \033[1;35mODD\033[m numbers are: \033[1;31m{numbers[1]}\033[m')
