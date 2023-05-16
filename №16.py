m = [[1, 2, 9],
     [7, 3, 5],
     [8, 4, 6]]
ma = float('-inf')
for i in range(len(m)):
    ma = max(ma, m[i][i], m[i][len(m) - 1 - i])
max_,k = m[0][0],0
for i in range(len(m)):
    if m[i][k] > max_:
        max_ = m[i][k]
    k += 1
print(max_)
print(ma)
