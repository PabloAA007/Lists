# -*- coding: utf-8 -*-
"""
Student Do: Grocery List.

This script showcases basic operations of Python Lists to help Mike
organize his grocery shopping list.
"""

# @TODO: Create a list of groceries
print("List of groceries: ")
groceries = ["Water", "Butter", "Eggs", "Apples", "Cinnamon", "Sugar", "Milk"]
print(groceries)
print("--------------------------------------------------")

# @TODO: Find the first two items on the list
print("Finding the first two items from the list: ")
print(groceries[:2])
print("--------------------------------------------------")

# @TODO: Find the last five items on the list
print("Finding the last five items on the list: ")
print(groceries[2:])
print("--------------------------------------------------")

# @TODO: Find every other item on the list, starting from the second item
print("Finding every other item on the list, starting from the second item")
print(groceries[1::2])
print("--------------------------------------------------")

# @TODO: Add an element to the end of the list
print("Adding Flour to the end of thew list")
groceries.append("Flour")
print(groceries)
print("--------------------------------------------------")

# @TODO: Changes a specified element within the list at the given index
print("Changing Apples on the list for Gala Apples")
groceries[3] = "Gala Apples"
print(groceries)
print("--------------------------------------------------")

# @TODO: Calculate how many items you have in the list
print("Calculating how many items are on the list")
print(len(groceries))
print("--------------------------------------------------")

# ----------------------Go to the grocery store---------------------------")

# @TODO: Find the index of the particular element name
print("Find the index of Gala Apples in the grocery list")
print(groceries)
print(groceries.index("Gala Apples"))
print("--------------------------------------------------")                      

# @TODO: Remove an element from the list based on the given element name
print("Removing sugar from the grocery list")
groceries.remove("Sugar")
print(groceries)
print("--------------------------------------------------")

# @TODO: Remove an element from the list based on the given index
print("Removing water using the index on the list")
water = groceries.index("Water")
groceries.pop(water)
print(groceries)
print("--------------------------------------------------")

# @TODO: Remove the last element of the list
print("Removing the last element of the list using the index")
groceries.pop(-1)
print(groceries)
print("--------------------------------------------------")
print("You continue on your journey purchasing groceries...")
