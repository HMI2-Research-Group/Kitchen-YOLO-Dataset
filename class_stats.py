import glob
from collections import defaultdict
from prettytable import PrettyTable


# read classes.txt and in each new line find the class name and it's index and save them to dictionary
class_dict = {}
curr_index = 0
for line in open("classes.txt"):
    line = line.strip()
    if line:
        class_dict[curr_index] = line
        class_dict[line] = curr_index
        curr_index += 1
# pretty print the dictionary
# print(class_dict)

all_labels = glob.glob("labels/*.txt")
count_dict = defaultdict(int)
for each_label_file in all_labels:
    # read each line in the label
    for line in open(each_label_file):
        line = line.strip()
        if line:
            # find the class name from the class_dict and increment the count
            # Split the line based off of whitespace
            class_number = int(line.split()[0])
            count_dict[class_dict[class_number]] += 1

# pretty print the count_dict
table = PrettyTable()
table.field_names = ["Class", "Count"]

# arrange the table in ascending order
for key, value in sorted(count_dict.items(), key=lambda item: item[1]):
    # Uncomment below to print so that you can add it to online sheets
    # for making latex tables
    # print(f"{key}\t{value}")
    table.add_row([key, value])

# Printing the table
print(table)
