"""
- A Set is a collection which is unordered and unindexed. No duplicate members.
- immutable
"""


set1 = {"Roger", "Syd"}
set2 = {"Roger"}

# intersect two sets/ All the common items
print(set1 & set2) # {'Roger'}

# union/ All the items and duplicate will be count as 1
print(set1 | set2) # {'Syd', 'Roger'}

# difference
print(set1 - set2) # {'Syd'}

# superset
print(set1 > set2) # True

# how many items
print(len(set1)) # 2

# get set as list
print(list(set1)) # ['Syd', 'Roger']

# if a item in a set
print("Roger" in set1) # True


# can not have duplicate item
print({"Roger", "Syd", "Roger"}) # {'Roger', 'Syd'}
