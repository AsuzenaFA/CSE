'''
# REVIEW
print("Hello World")
# the
car = 5
driving = True
print("I have %s cars" % car)
print("I have " + str(car) + " cars")

age = input("How old are you? 4")
print(age + "! your that old.")

colors = ["brown", "gray", "pink", "blue", "purple"]
colors.append("green")
print(colors)
colors.pop(0)
print(colors)
print(len(colors))
print(colors[1])
'''
# Dictionary Notes
states = {

'''
print(states["CA"])
print(states["NV"])
'''
nested_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 5092030
    }
}
'''
print(nested_dictionary["NV"]["POPULATION"])
print(nested_dictionary["RI"]["NAME"])
'''
complex_dictionary = {
    "CA": {
        "NAME": "California",
        "POPULATION": 39540000,
        "CITIES": [
            "Fresno",
            "San Francisco",
            "Los Angeles"
        ]
    },
    "VA": {
        "NAME": "Virginia",
        "POPULATION": 8500000,
        "CITIES": [
            "Richmond",
            "Norfolk",
            "Alexandira"
        ]
    },
    "MD": {
        "NAME": "Maryland",
        "POPULATION": 6000000,
        "CITIES": [
            "Bethesda",
            "Baltimore",
            "Annapolis"
        ]
    },
    "RI": {
        "NAME": "Rhode Island",
        "POPULATION": 1057315,
        "CITIES": [
            "Providence",
            "Newport",
            "Warwick"
        ]
    },
    "NV": {
        "NAME": "Nevada",
        "POPULATION": 5092030,
        "CITIES": [
            "Carson City",
            "Las Vegas",
            "Reno"
        ]
    }
}
'''
print(complex_dictionary["RI"]["CITIES"][2])

print(complex_dictionary["VA"]["NAME"])
print(complex_dictionary["MD"]["CITIES"][0])

# .keys gives keys in dictionary
print(complex_dictionary.keys())
print(nested_dictionary.items())

print()
for key, value in complex_dictionary.items():
    print(key)
    print(value)
    print("-" * 20)


for state, facts in complex_dictionary.items():
    for attr, value in facts.items():
        print(attr)
        print(value)
        print("-" * 20)
    print("=" * 20)
'''
# adding to a dictionary

states['AL'] = "Alaska?"  # It isn't Alaska

# Changing a dictionary Value

states['Al'] = "Alabama" # it's actually Alabama