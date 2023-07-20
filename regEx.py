import re

x = input("input: ")

list = ["green_apple", "red_apple", "blue_apple"]
y = re.search(x + r"_.+", str(list))

if y:
	print("match")
else:
	print("no match") 