from collections import Counter
input_data = """

""".strip()

lines = input_data.split('\n')
left_list = []
right_list = []

for line in lines:
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

left_list.sort()
right_list.sort()

total_distance = sum(abs(a-b) for a,b, in zip(left_list,right_list))
print(total_distance)


count  = Counter(right_list)

sum = 0
for num in left_list:
    sum += num * count[num]

print(sum)

