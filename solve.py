import numpy


def solve(file):
	handle = open(file, 'r')
	row = int(handle.readline())
	col = int(handle.readline())
	b = [float(x) for x in handle.readline().split()]
	A = []
	for i in range(0, row):
		A.append([float(x) for x in handle.readline().split()])
	handle.close()

	x = numpy.linalg.lstsq(A, b, rcond=None)

	return x


