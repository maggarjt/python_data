FUNCTIONS

# def defines code and remembers, does not run until called 
#calling involves parameters according to structure of function
# structure vs invoking


def thing():
	print('Thing called')
	print('You rang?"')


thing()   # this is the call with no parameters
print('again!')
thing()
# will call thing twice with again printed in between lines

Thing called
You rang?
again!
Thing called
You rang?


# FUNCTION TYPES    BUILT IN AND DEFIONED FUNCTIONS
# int(), float(), print() etc are built in functions
# def used to create methods, class used to create classes which contain methods

BUILT IN EXAMPLES
big = max('Hello world')
#max function knows its a string and will look for lexigraphically biggest character
# order lowercase has higher value than uppercase so 'w' is stored in memory location designated by variable big

tiny = min('Hello world')
#returns the blank space

----------------------------------------------------------------------------------
#ARGUMENTS and parameters, they allow more functionality in more situations
big = max('Hello world')


# define function, it is NOT called until you invoke it
def greet(lang):
	if lang == 'es'
		print('Hola')
	elif lang == 'fr'
		print('Bonjour')
	else:
		print('Hello')


greet()  #calls without parameters will get an error due to requirements of the arguments being present
# you can fix this with defaults

greet('es')

#will print Hola

-----------------------------------------------------------------------------
RETURN

def greet():
	return "Hello"

print(greet(), "Jesse")
# returns Hello and concatenates Jesse string

# return is used to evaluate a value by returning information creating a residual value
#fruitful function return values, function auto returns at end

# rewrite greet function to use returns, return ends function and provides fruitful residual value
def greet(lang):
	if lang == 'es'
		return('Hola')                                        
	elif lang == 'fr'
		return('Bonjour')
	else:
		return('Hello')



print(greet('en'), 'Glenn')
#returns Hello Glenn
print(greet('es'), 'Juan')
#returns Hello Glenn

-------------------------------------------
MULTIPLE parameters 

def combiner(a, b):
	return a + b

combiner(3,5)
9
combiner(9,8) # a = 9, b=8
17