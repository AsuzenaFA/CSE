string1 = "apples"
list1 = list(string1)
print("- - - - - -")
print(input("Take a guess' '"))
for character in list1:
    if character == "a":
        current_index = list.index(character)
        list1.pop(current_index)
        list.insert(current_index, "*")
