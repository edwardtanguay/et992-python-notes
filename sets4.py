set1 = {'red', 'blue', 'yellow', 'blue', 'red', 'green'}
set2 = {'blue', 'chartreuse', 'amber', 'red'}

print("\n// SETS")
print(set1)
print(set2)
print("\n// ALL ELEMENTS FROM BOTH SETS WITHOUT DUPLICATES")
print("union", set1.union(set2))
print("union", set1 | set2)
print("\n// IN BOTH SETS")
print("intersection", set1.intersection(set2))
print("intersection", set1 & set2)
print("\n// IN FIRST SET BUT NOT IN SECOND")
print("difference", set1.difference(set2))
print("difference", set1 - set2)
print("\n// EITHER IN FIRST OR SECOND BUT NOT IN BOTH")
print("symmetric_difference", set1.symmetric_difference(set2))
print("symmetric_difference", set1 ^ set2)