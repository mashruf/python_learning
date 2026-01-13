# break and continue works in both for and while loop

# continue
items = [1,2,3,4]

for item in items:
    if item == 2:
        continue
    print(item) # 1 3 4

# break

for item in items:
    if item == 2:
        break
    print(item) # 1 