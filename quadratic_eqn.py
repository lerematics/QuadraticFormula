import math
class Quadratic:
	
	def __init__(self, a = 0, b = 0, c = 0):
		self.a = a
		self.b = b
		self.c = c
		
	def formula(self):
		root_1 = (-self.b + math.sqrt(self.b**2 - 4 * self.a * self.c)) / (2 * self.a)
		root_2 =  (-self.b - math.sqrt(self.b**2 - 4 * self.a * self.c)) / (2 * self.a)
		
		return '\n==> Quadratic roots are {:.2f} and {:.2f}'.format(root_1, root_2)

while True:
	try:
		a = float(input(">>> Enter the coefficient of x² i.e 'a': "))
		break
	except:
		print('..input must be a float or an integer ...')
		
while True:
	try:
		b = float(input(">>> Enter the coefficient of x i.e 'b': "))
		break
	except:
		print('..input must be a float or an integer ...')
	
while True:
	try:
		c = float(input(">>> Enter the coefficient of x^0 i.e 'c': "))
		break
	except:
		print('..input must be a float or an integer ...')

quadratic = Quadratic(a, b, c)
print(quadratic.formula())