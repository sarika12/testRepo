def get_divide():
	r=0
	max=1000

	for i in range(0,max):
		if i%3==0 or i%5==0:
			r+=i
		print r
