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

new_list = ["eggs", "cheese", "oranges", "raspberries"]
new_list[2] = "apples"
print("The last thing in the list is %s" % new_list[len(new_list)-1])

# Getting part of a list
print(new_list[1:3])
print(new_list[1:4])
print(new_list[1:])
print(new_list[:2])


# Adding thing to a list
holiday_list = []
holiday_list.append("Tacos")
holiday_list.append("bumblebee")
holiday_list.append("Red Dead Redemption 2")
print(holiday_list)

# Notice this is an "object.method(Parameters)

# Removing thing from the list
holiday_list.remove("Tacos")
print(holiday_list)


gift_list = ["switch", "PS4", "Xbox one"]
print(gift_list)
gift_list.append("3DS")
print(gift_list)

# ALSO removing thing from a list
holiday_list.pop(0)  # Removes the item at index 0
print(holiday_list)

colors = ['red', 'bue', 'yellow', 'green', 'purple', 'pink', 'brown', 'white', 'black', 'cyan', 'gray', 'teal', 'olive'
          'aqua', 'sky blue', 'crimson', 'turquoise']
print(len(colors))
# Find the index
print("brown")

string1 = "turquoise"
list1 = list(string1)
print(list1)

# Changing lists into strings
print("!".join(list1))

for character in list1:
    if character == "u":
        # replace it with a star*
        current_index = list.index(character)
        list1.pop(current_index)
        list.insert(current_index,"*")

# Function practice
# a**2 + b**2 = c**2
def pythagorean(a, b):
    return(a**2 + b**2)**(1/2


pythagorean(3, 4)

'''