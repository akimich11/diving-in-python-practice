import sys

if __name__ == "__main__":
	steps = int(sys.argv[1])
	for i in range(1, steps + 1):
		print(" " * (steps - i) + "#" * i)
