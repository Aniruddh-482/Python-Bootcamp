# Slincing in Python #
# ------------------ #

# Slicing in Python is a feature that enables accessing parts of sequences like strings, tuples, and lists.

# How to Slice Lists & Tuples in Python:
#         From   To
#           \   /
# piano_keys[2:5]
#      |
# List/Tuple

# For Example: 

# Slicing of Lists
# ---------------- #
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]

print(piano_keys[2:5])
# Output: ['c', 'd', 'e']

print(piano_keys[2:])
# Output: ['c', 'd', 'e', 'f', 'g']

print(piano_keys[:5])
# Output: ['a', 'b', 'c', 'd', 'e']

print(piano_keys[2:5:2])
# Output: ['c', 'e']

print(piano_keys[::2])
# Output: ['a', 'c', 'e', 'g']

print(piano_keys[::-1])
# Output: ['g', 'f', 'e', 'd', 'c', 'b', 'a']

# Slicing of Tuples #
# ----------------- #
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")

print(piano_tuple[2:5])
# Output: ('mi', 'fa', 'so')

print(piano_tuple[1:])
# Output: ('re', 'mi', 'fa', 'so', 'la', 'ti')
