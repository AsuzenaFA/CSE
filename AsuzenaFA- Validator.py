import csv


def reverse(num: list):
    print(num[::-1])


def multiply(num: list):
    fro index % 2 =-


def last_num_begone(num: list):
    _last_num = int(num[16])
    if last_num == [15]:


with open("Book1.csv", 'r') as old_csv:
    with open("MyNewFile.csv", 'w', newline='') as new_csv:
        reader = csv.reader(old_csv)
        writer = csv.writer(new_csv)
        print("Processing...")

        for row in reader:
            old_number = row[0]
            numbers = list(old_number)

            if len(numbers) == 16:
                last_num = numbers[15]
                numbers.remove(last_num)
                reverse(numbers)


                writer.writerow(row)
        print("OK")