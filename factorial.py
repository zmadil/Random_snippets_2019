n=5

def rec_fac(n):
	if n==1:
		return 1
	
	else:
		return n*rec_fac(n-1)

print (rec_fac(n))