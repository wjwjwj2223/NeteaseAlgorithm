
inputs = input()
goods = inputs.split(" ")
goods = list(map(lambda a: int(a), goods))

money = input()
totalMoney = int(money)

def consume(goods, totalMoney):
	if not totalMoney:
		return 1
	if totalMoney < 0:
		return 0

	for good in goods:
		tempGoods = goods.copy()
		tempTotalMoney = totalMoney
		tempGoods.remove(good)
		tempTotalMoney = totalMoney - good
		done = consume(tempGoods, tempTotalMoney)
		if done:
			return 1
	return 0


if not consume(goods, totalMoney):
	print('False')
else:
	print('True')