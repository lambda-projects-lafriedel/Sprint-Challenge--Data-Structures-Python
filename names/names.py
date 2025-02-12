import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# Given code:
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# Code optimization:
# For each name in names_1, insert name into a binary search tree
bst_names = BinarySearchTree(names_1[0])
for name1 in names_1:
    bst_names.insert(name1)

# For each name in names_2, check if bst contains name.
for name2 in names_2:
    # If true, append name from names_2 to duplicates
    if bst_names.contains(name2):
        duplicates.append(name2)

duplicates.sort()

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

