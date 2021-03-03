#x = [1,2,3,4,5]
x = (i*2 for i in range(10) if i%3)
for elem in x:
    print elem
