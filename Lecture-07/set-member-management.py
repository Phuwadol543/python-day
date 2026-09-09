fruits = {"apple","banana","cherry"}

fruits.add("apple")
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

fruits.add("banana")
print(fruits)  # Output: {'banana', 'cherry', 'apple'}

fruits.add("kiwi")
print(fruits)  # Output: {'banana', 'cherry', 'apple', 'kiwi'}

removed_item = fruits.pop()
print("Removed item:", removed_item)
print("Set after removal:", fruits)

fruits.clear()
print(fruits)  # Output: set(0)