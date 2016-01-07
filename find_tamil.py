inputfile = 'words'

input = open(inputfile,'r')
out = open('tamil-words.txt','w')

def is_tamil(word):
	word = word.decode('utf-8')
        first_char = word[:1]
        lang_number = ord(first_char)
        if lang_number >= 2944 and lang_number <= 3071:
		return True
	
	
for line in input.readlines():
	try:
		if is_tamil(line):
			print line
			out.write(line)

	except Exception, e:
		print " "
	

input.close()
out.close()



tamil_words_set = set(map(str.strip, open('tamil-words.txt')))
uniq_words = open('only_uniq_tamil_words.txt','w')

for word in tamil_words_set:
	uniq_words.write(word)
	uniq_words.write("\n")
uniq_words.close()


