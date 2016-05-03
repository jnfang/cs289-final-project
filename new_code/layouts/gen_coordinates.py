import random

def new_xy(mmin, mmax):
	x = random.randint(mmin, mmax)
	y = random.randint(mmin, mmax)
	while y == x:
		y = random.randint(mmin, mmax)
	return (x, y)

def print_coors(mmin, mmax):
	found = {}
	for i in xrange(45):
		newx, newy = new_xy(mmin, mmax)
		while (newx, newy) in found:
			newx, newy = new_xy(mmin, mmax)
		print "queue.push(Package(({},{}), 1), 1)".format(newx, newy)



if __name__ == "__main__":
	print_coors(1, 38)