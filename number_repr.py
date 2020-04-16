x = 10_000_000
y = 1_000_000_000_000

total = num1 + num2

print(total)


#hard to read the numbers, add commas by underscoring and changing the underscores later
# underscore does not change the math, it is replaced in f string formatting via the colon :

print(f'{total:r}')
