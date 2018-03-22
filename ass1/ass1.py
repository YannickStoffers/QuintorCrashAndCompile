from sys import stdin

def boringDigit (digit):
	while digit >= 10:
		digit = sum (map (int, list (str (digit))))
	return digit

def concat (n, k):
	num = ''
	while k:
		num += str (n)
		k -= 1
	return int (num)

n, k = map (int, stdin.readline ().strip ().split ())
print (boringDigit (concat (n, k)))
