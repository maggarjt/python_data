# try/except is a way to avoid code errors and traceback calls as well as program interruption
#use when you can anticipate for difficulties in program 


astring = 'Hey man!'

try:
	istr = int(astr)
except:
	istr = -1

print('First', istr)

#will print   First -1    due to conversion type error with int()

--------------------------------------------------------------------------

astr = 14566

try:
	istr = int(astr)
except:
	istr = -1

print('Second', istr)

# will print Second 14566