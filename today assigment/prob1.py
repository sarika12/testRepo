'''it will give you in a file how many line charecter and word'''
import sys
def wlc_count(file_name):
	char_count = 0
	f = open(file_name).read()
	count_space = f.count(' ')
	word_list = f.split()
	for word in word_list:
		char_count += len(word)
	word_count = len(word_list)
	line_count = len(f) - count_space - char_count
	
	print 'LINE==>',line_count
	print 'WORD==>',word_count
	print 'CHAR==>',char_count



if __name__ == '__main__':
	wlc_count(sys.argv[1]) 
