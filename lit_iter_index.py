#returning index and list name via enumerate function to unpack list and pair with index

names = ['Corey', 'Chris', 'Dave', 'Travis' ]

index = 0
for name in names:
	print(index, name)
	index += 1

#correct but not clean or concise



#enumerate returns an object of type enumerate ex. [(0, Tom), (1, Billy)]   ---list of tuples
# which can be used in loops or converted into list of tuples using list() 
# if used on strings it splits the string into characters ex. enumerate(iterable, start_index)
names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
for index, name in enumerate(names):
	print(index, name)
	




#looping over two lists at once with enumerate
#not intuitive

names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']

for index, name in enumerate(names):
	hero = heroes[index]
	print(f'{name} is actually {hero}')



#looping over two lists at once with zip
# more intuitive  zip()  maps similar indexes of multiple iterable containers to use as single entity
#   zip(iterators)   -  list, string..etc
#returns single iterator object mapped from values from each
#   set(any iterable sequence) used with str() to print
# set iterates through and removes duplicates returning a set


names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']


for name, hero in zip(names, heroes):
	print(f'{name} is actually {hero}')


# if used on dictionary the values are lost and set only affects keys, dic cant have duplicate keys so not sure where this is useful

dic1 = {4:'geeks', 3:'jocks', 2:'nerds', 7:'swans'}
print(" The dictionary before set conversion is: " + str(dic1))
print(" The dictionary after set conversion is: " + str(set(dic1)))



# f strings are quicker and doesnt hide code inside string that wont be syntax-checked until run time
# f strings also allow you to put function or method calls directly, can even put calculations inside

def to_lower(input):
	return input.lower()
def age_in_two(age):
	return age + 2


name = 'BARRY'
age = 27

print(f'{to_lower(name)} has a lowercase name')
print(f'He is {age_in_two(age)} years old')


names = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Spiderman', 'Superman', 'Deadpool', 'Batman']
universe = ['Marvel', 'DC','Marvel', 'DC' ]

for name, hero, universe in zip(names, heroes, universe):
	print(f'{name} is actually {hero} in the {universe} universe')