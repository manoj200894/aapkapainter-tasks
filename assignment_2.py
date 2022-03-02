arr = [1,2,3,2,1]
d = {}

even = []
odd = []
for i in arr:
    if i % 2 == 0:
        even.append(i)
        d['p1'] = sum(even)

    else:
        odd.append(i)
        d['p2'] = sum(odd)

print(d)












