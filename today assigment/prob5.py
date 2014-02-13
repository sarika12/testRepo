'''it will add differant kind of element and also change data type'''

def convert(fun):
	def inner(*arg):
		list2 = list(arg)
		list3 = []
		x = type(list2[0])
		try:
			for i in list2:
				list3.append(x(i))
			arg = tuple(list3)
			return fun(*arg)
		except Exception:
			print 'Zeomega Error 123:........'
	return inner


@convert
def total(*arg):
	if type(arg[0]) is int:
		sum1 = 0 
	elif type(arg[0]) is str:
		sum1 = ''
	elif type(arg[0]) is list:
		sum1 = []
	elif type(arg[0]) is dict:
		raise TypeError,'we canot add two dictionary'
	elif type(list1[0]) is tuple:
		sum1 = ()
	for element in arg:
		sum1 +=element
	print 'Result==>',sum1







