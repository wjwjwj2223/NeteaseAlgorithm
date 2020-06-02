
def frogStep(count):
	if count == 1:
		return 1
	if count == 2:
		return 2
	return frogStep(count - 1) + frogStep(count - 2)
for i in range(1,10):
	print(frogStep(i))
