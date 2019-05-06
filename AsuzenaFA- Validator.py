import csv


def reverse(num: list):
    digits = (num[::-1])
    return digits


def multiply(num: list):
    for index in range(len(num)):
        num[index] = int(num[index])
        if index % 2 == 0:
            num[index] *= 2

        if num[index] > 9:
            num[index] -= 9
    return num


def add_all(my_list: list):
    total = 0
    for digit in my_list:
        total += int(digit)
    return total


def validate(digits: list):
    if len(digits) == 16:
        last_digit = digits.pop(15)
        reversed_nums = reverse(digits)
        multiplied = multiply(reversed_nums)
        sum1 = add_all(multiplied)
        return sum1 % 10 == int(last_digit)
    return False


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            digits = list(old_number)

            if validate(digits):
                writer.writerow(row)
        print("OK")
