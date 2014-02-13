import sys
def is_prime(a):
	ram=reduce(list.__add__,[[i,a//i] for i in range(1,int(a**0.5)+1) if a%i==0])
	if len(ram)==2:
		return True
	else:
		return False
def funct(a):
	list1=[]
	ram=reduce(list.__add__,[[i,a//i] for i in range(1,int(a**0.5)+1) if a%i==0])
	
	for i in ram:
		if is_prime(i):

			list1.append(i)
	
	print max(list1)

if __name__  == '__main__':
	funct(int(sys.argv[1]))
					
