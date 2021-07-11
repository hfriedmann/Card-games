import random

l = ["bee", "wasp", "ant", "fly", "bug", "spider"]

list1 = (random.sample(l, 3))

test_keys = ["1", "2", "3"]
test_values = list1

# Printing original keys-value lists
print("Original key list is : " + str(test_keys))
print("Original value list is : " + str(test_values))

# using zip()
# to convert lists to dictionary
dictionary = dict(zip(test_keys, test_values))

# Printing results
print("Resultant dictionary is : " + str(dictionary))
print("first item is:", dictionary["1"])
