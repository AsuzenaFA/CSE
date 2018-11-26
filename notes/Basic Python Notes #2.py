'''
# Lists
shopping_list = ["whole milk", "PC", "Eggs", "Xbox One", "PS4"]
print(shopping_list)
print(shopping_list[0])
print("The second thing in the list is %s" % shopping_list[1])
print("The length if the list is %d" % len(shopping_list))

# Changing Elements in a list
shopping_list[0] = "2% milk"
print(shopping_list)
print(shopping_list[0])

# Looping through lists
for item in shopping_list:
    print(item)


grocery_list = ["Kale", "Peanut Butter", "Skim milk", "Banana"]
print(grocery_list)
grocery_list[2] = "Almond milk"
print(grocery_list[2])
print(grocery_list)
'''
new_list = ["eggs", "cheese", "oranges", "raspberries"]
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list)-1])

# Getting part of a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:2])

