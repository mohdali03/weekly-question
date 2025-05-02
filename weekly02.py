# 1. Two Sum
"""
nums = [2,7,11,15]
target = 9

n = len(nums) - 1 
for i in range(n):
	for j in range(i+1, n):
		if nums[i] + nums[j] == target:
			print([i,j])
			break

"""

# 2. Valid Parentheses
def sol():
	s = "(}"

	# h = {")" : -1, "(" : 1, "}": -1, "{": 1, "[": 1, "]" : 1}
	h = {")" : "(", "}" : "}", "]": "["}

	result = []
	for i in s:
		if i in h:
			if len(result) == 0:
				return False
				break
			if result[-1] == h[i]:
				result.pop()
		else:
			result.append(i)

	return len(result) == 0
print(sol())

# 3. Compare The Triplets
'''
a = [5,6,7]
b = [3,6,10]


ar = 0
br = 0

for i in range(len(a)):
	
	if a[i] > b[i]:
		ar +=1
	elif a[i] < b[i]:
		br +=1

print([ar,br])
'''


# 4. Excel
"""
column = "ZY"

result = 0

for i in column:
	result = result * 26 + ord(i) - 64

print(result)

"""

# 5. Convert 12 Hours

'''

s = "12:05:45AM"
format = s[-2:]
time = int(s[:2])
s = s[2:-2]
print(format, time, s)


if time == 12:
	time = 0
if format == "PM":
	
	time +=12  

print(str(time)+ s)
'''