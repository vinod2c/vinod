a = input("enter first value:")
b = input("enter second value:")
try:
	c = a/b
except Exception as e:
	print "division is not possible"
	print str(e)
	c = 0
print c
