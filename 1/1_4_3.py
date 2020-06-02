

def consume(goods, index, target):
	if not target:
		return True
	elif index == 0:
		return goods[index] == target
	elif goods[index] > target:
		return False
	else:
		return consume(goods, index - 1, target - goods[index]) or consume(goods, index - 1, target)


inputs = input()
goods = inputs.split(" ")
goods = list(map(lambda a: int(a), goods))

index = len(goods) - 1
money = input()
totalMoney = int(money)

print(consume(goods, index, totalMoney))