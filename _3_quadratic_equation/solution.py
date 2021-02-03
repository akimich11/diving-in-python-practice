import sys

if __name__ == "__main__":
	a = int(sys.argv[1])
	b = int(sys.argv[2])
	c = int(sys.argv[3])

	print((-b + (b ** 2 - 4*a*c) ** 0.5) / (2 * a))
	print((-b - (b ** 2 - 4*a*c) ** 0.5) / (2 * a))
