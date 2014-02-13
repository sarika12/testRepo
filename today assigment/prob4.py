'''it will remove consucative number from the list'''

def remove_one(list1):
	print 'orignal list==>',list1
	a = 0
	while len(list1) != a:
		if len(list1) > (a + 2) and list1[a]+1 == list1[a+1] and list1[a+2] == list1[a] + 2 :
			list1.pop(a)
		elif len(list1) > (a+1) and list1[a]+1 == list1[a+1]:
			list1.pop(a)
			list1.pop(a)
		else:
			a += 1
	print 'Modified list==>',list1


'''it will remove consucative duplicate element from list'''
 
def remove_cons_dup(list1):
	print 'orignal list==>',list1
	a = 0
	while len(list1) != a:
		if list1[a] == list1[a+1]:
			list1.pop(a)
			a += 1
		else:
			a += 1
	print 'Modified list==>',list1
	
	
