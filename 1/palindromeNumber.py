
def palindromeNumber(cascode):
	if cascode < 10:
		print(cascode)
	else:
		print(cascode)
		palindromeNumber(cascode // 10)
		print(cascode)

palindromeNumber(12345)