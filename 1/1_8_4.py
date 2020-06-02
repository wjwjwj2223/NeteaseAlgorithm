import copy

def combination(arr, count):
    result = []
    temp = [0] * count

    def loop(ni=0, nc=0):
        if nc > count:
            return
        if nc == count:
            print(temp)
            return
        for idx in range(ni, len(arr)):
            temp[nc] = arr[idx]
            loop(idx+1, nc+1)
    loop()
    return result

if __name__ == '__main__':
	
    combination([1,2,3,4,5], 2)