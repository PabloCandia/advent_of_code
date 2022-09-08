def read_file(filename):
    with open(filename, "r") as document:
        doc = [x.replace("\n", ",") for x in [line.strip("\n") for line in document.read().split("\n\n")]]
    return doc

def answer_set(group):
    return set(list(group.replace(",", "")))

def yes_everyone(group):
    yes_count_group = 0
    for char in answer_set(group):
        everyone = 1
        for person in group.split(","):
            everyone *= int(char in person)
        if everyone == 1: yes_count_group += 1
    return yes_count_group
    
def part_1(filename):
    yes_count = 0
    for group in read_file(filename): yes_count += len(answer_set(group))
    return yes_count

def part_2(filename):
    yes_count = sum([yes_everyone(group) for group in read_file(filename)])
    return yes_count

if __name__ == "__main__":
    print("Enter the name of the file:")
    filename = input()
    print("The total number of 'yes' answers is {}.".format(part_1(filename)))
    print("The total number of 'yes' answers by everyone in each group is {}.".format(part_2(filename)))
    
    
