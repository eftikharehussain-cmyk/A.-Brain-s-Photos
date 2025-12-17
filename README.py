# A.-Brain-s-Photos
n, m = map(int, input().split())
_matrix = []
count = 0
for i in range(n):
	rows = list(input().split())
	_matrix.append(rows)
for j in range(len(_matrix)):
	for k in range(len(_matrix[j])):
		if _matrix[j][k] == 'C' or _matrix[j][k] == 'M' or _matrix[j][k] == 'Y':
			count += 1
if count > 0:
	print('#Color')
else:
	print('#Black&White')
