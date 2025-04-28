
# 1. best stock
prices = [7,1,5,3,6,4]

prices = [7,6,4,3,1]


best = 0

for i in range(len(prices)-1):
	for j in range(i + 1, len(prices)-1):
		if prices[i] < prices[j]:
			current  = prices[j] - prices[i]

			if best < current:
				best = current
print(best)







# 2.Squares of a Sorted Array


nums = [-4,-1,0,3,10]



left = 0
right = len(nums)-1 
pos = len(nums)-1

result = [0] * 5


while left <right:
	right_ans = nums[right] **2
	left_ans = nums[left] ** 2
	if left_ans < right_ans:
		result[pos] = right_ans
		right -=1
	else:
		result[pos] = left_ans
		left+=1
	pos -=1

print(result)





# 3. find the word 



inp = "hello zoo sun"

max_value = 0

maxs = ""

for i in inp.split(" "):
	current = 0

	for v in i:
		current += ord(v)
		
	current = current / len(i)
	
	if current > max_value:
		max_value = current
		maxs = i


print(maxs)


# 5. Count Number 





inp = "HelloWorld"
cap = 0
small = 0

for i in inp:
	if i in "ABCDEFGHIJLKMNOPQRSTUVWXYZ":
		cap +=1
	else:
		small += 1


print(cap, small)























