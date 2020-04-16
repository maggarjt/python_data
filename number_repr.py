num1 = 10_000_000
num2 = 1_000_000_000_000

total = num1 + num2

print(total)

#returns hard to read number  1000100000001000000 


#hard to read the numbers, add commas by underscoring and changing the underscores later
# underscore does not change the math, it is replaced in f string formatting via the colon :

print(f'{total:,}')

#returns 1,000,000,000,000,000,000
