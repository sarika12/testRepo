'''it will give gcd and lcm for given n number'''

def gcd(a, b):
	if a < 0 or b < 0:
		return -1
	elif a>b:
		a, b = b, a

	while a:
		p = a
		a = b % a
		b = p
	return b

def lcm(a, b):
	x, y = a, b
	while x != y:
		if x > y:
			y += b
		else:
			x += a
	return x
	
		

def my_gcd(*arg):
	list1 = list(arg)
	l = gcd(list1[0], list1[1])
	for m in range(2, len(list1)):
		 l = gcd(l, list1[m])
	print 'gcd ==>',l
		

def my_lcm(*arg):
	list1 = list(arg)
	l = lcm(list1[0], list1[1])
	for m in range(2, len(list1)):
		 l = lcm(l, list1[m])
	print 'lcm ==>',l

	


	
