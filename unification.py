class FOL:
	def __init__(self, operation, argument):
		self.operation = operation
		self.argument = argument
	
	def constant(self):
		for arg in self.argument:
			if isvariable(arg):
				return False
			elif isinstance(arg, FOL):
				if not arg.constant():
					return False
		return True
	
	def replace(self, var, x):
		for i in range(len(self.argument)):
			if occur_check(var, self.argument[i]):
				if self.argument[i] == var:
					self.argument[i] = x
				else:
					self.argument[i].replace(var, x)
	
	def modify(self, theta):
		for i in range(len(self.argument)):
			arg = self.argument[i]
			if isvariable(arg) and arg in theta.keys() and isconstant(theta[arg]):
				self.argument[i] = theta[arg]
			elif isinstance(arg, FOL):
				self.argument[i].modify(theta)

	def print(self):
		output = self.operation + '('
		for arg in self.argument:
			if isinstance(arg, FOL):
				output += arg.print() + ','
			else:
				output += arg + ','
		output = output[:-1] + ')'
		return output

def isvariable(x):
	return isinstance(x, str) and x.islower()

def isconstant(x):
	if isinstance(x, str) and not x.islower():
		return True
	elif isinstance(x, FOL) and x.constant():
		return True
	else:
		return False

def islist(x):
	return isinstance(x, list)

def iscompound(x):
	return isinstance(x, FOL) and not x.constant()

def occur_check(var, x):
	if var == x:
		return True
	elif not isinstance(x, FOL):
		return False
	else:
		for arg in x.argument:
			if occur_check(var, arg):
				return True
		return False

def unifyvar(var, x, theta):
	if not isinstance(theta, dict):
		return f'Error while unifying variable {var} and {x}'
	if var in theta.keys():
		return unify(theta[var], x, theta)
	elif x in theta.keys():
		return unify(var, theta[x], theta)
	elif occur_check(var, x):
		return 'Fail'
	else:
		new_theta = {}
		x_constant = isconstant(x)
		for k in theta.keys():
			if x_constant and isinstance(theta[k], FOL):
				new_theta[k] = theta[k].replace(var, x)
			else:
				new_theta[k] = theta[k]
		if not x_constant and isinstance(x, FOL):
			x.modify(new_theta)
		new_theta[var] = x
		return new_theta

def unify(x, y, theta={}):
	if theta == 'Fail':
		return 'Fail'
	elif x == y:
		return theta
	elif isvariable(x):
		return unifyvar(x, y, theta)
	elif isvariable(y):
		return unifyvar(y, x, theta)
	elif iscompound(x) and iscompound(y):
		return unify(x.argument, y.argument, unify(x.operation, y.operation, theta))
	elif islist(x) and islist(y):
		return unify(x[1:], y[1:], unify(x[0], y[0], theta))
	else:
		return 'Fail'

def print_result(result):
	if isinstance(result, str):
		print(result)
	else:
		output = '{'
		for (k,v) in result.items():
			if isinstance(v, FOL):
				output += k + '/' + v.print() + ','
			else:
				output += k + '/' + v + ','
		output = output[:-1] + '}'
		print(output)

if __name__ == '__main__':
	fol1 = FOL('Knows', ['John', 'x'])
	fol2 = FOL('Knows', ['y', FOL('Know', ['z', FOL('Mother', ['y'])])])

	result = unify(fol1, fol2)
	print_result(result)