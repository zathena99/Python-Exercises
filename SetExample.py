#SetExample
# Create two sets

set1 = {"ALISTAR", "BRAUM", "GALIO", "PANTHEON", "TAMH KENCH"}
set2 = {"JANNAH", "THRESH", "KARMA", "TAMH KENCH", "GALIO"}

# Print the sets
print("\nTank Champions:", set1, "\n")
print("Support Champions:", set2)

# Union of sets
union_set = set1.union(set2)
print("\nUnion of sets:", union_set)

# Intersection of sets
intersection_set = set1.intersection(set2)
print("Intersection of sets:", intersection_set)

# Difference of sets (elements in set1 but not in set2)
difference_set = set1.difference(set2)
print("Difference of sets (set1 - set2):", difference_set)

# Difference of sets (elements in set2 but not in set1)
difference_set2 = set2.difference(set1)
print("Difference of sets (set2 - set1):", difference_set2)
