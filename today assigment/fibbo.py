def fibbo(n):
	a=0
	b=1
	tot=0
	for i in range(n ** 0.5):
		
		c=a+b
		if c>=4000000:
			break
		if c % 2 == 0:
			tot += c

		a=b
		b=c
		
		print c
	print 'total==>',tot
