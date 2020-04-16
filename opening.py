#opening files without having to close
# simple way of opening with closing manual

#f variable strores opened data, r is read rights flag
#new variable stores data opened previously
#  close() method performed after operations have been done, manually enetered

f = open('test.txt, r')

file_contents = f.read()

f.close()



#----------------------------------------------------------------------------------------------------------

#python built in function closes file without coding and file_contents variable can be manipulated
# for example splitting the string by "" delimiter , counting and printing results


with open('test.txt', r) as f:
	file_contents = f.read()


words = file_contents.split("")
word_count = len(words)
print(word_count)
