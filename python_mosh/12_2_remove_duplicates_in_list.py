arr = [0,1,2,3,3,3,2,4,1,5,4,3,2,5,6,2,1,0,6]

res = []
for i in arr:
    if i not in res:
        res.append(i)

print(res)