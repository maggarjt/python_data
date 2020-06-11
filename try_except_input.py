try/except 

rawstr = input('Enter number')
#input converted from str to int

try:
	ival = int(rawstr)
except:
	ival = -1


if ival > 0:
	print('Nice Work')
else:
	print('Not a number')

	#rough example    if input == -1 then the code fails due to programmer error
	#not sound code but the example is valid