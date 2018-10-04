import sympy as sp


def get_vars(n):
	vars = []
	for i in range(n):
		vars.append([])

	xs = 'x1'
	for i in range(2, n+1):
		xs += ' x' + str(i)

	vars = sp.symbols(xs)
	return vars


def solve(file):
	handle = open(file, 'r')
	row = int(handle.readline())
	col = int(handle.readline())
	b = sp.Matrix([float(x) for x in handle.readline().split()])
	system = sp.Matrix(([]))
	for i in range(0, row):
		A = sp.Matrix([[float(x) for x in handle.readline().split()]])
		system = system.col_join(A)
	handle.close()

	system = system.row_join(b)

	vars = get_vars(col)

	x = sp.solve_linear_system(system, *vars)
	return x


