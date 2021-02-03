import sys

if __name__ == "__main__":
	digit_string = sys.argv[1]
	digit_sum = 0
	for symbol in digit_string:
		digit_sum += int(symbol)
	print(digit_sum)
