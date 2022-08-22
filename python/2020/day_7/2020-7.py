def parse_rules(rule):
    # This function parses each one of the rules as given by an enumeration of the contents of each bag
    items = rule.split(', ')
    return [item.split(' ')[0] for item in items], [" ".join(item.split(' ')[1:-1]) for item in items]
    
def rule_dict(filename):
    # This function reads the file and creates a dictionary with the rules
    rules = {}
    with open(filename, "r") as file:
        for line in file:
            colour, rule = line.split(" bags contain ")
            numbers, contents = parse_rules(rule)
            if numbers[0]=="no":
                rules[colour] = 0
            else:
                rules[colour] = {}
                for i,content in enumerate(contents):
                    rules[colour][content] = int(numbers[i])
    return rules

def outer_bags(bag_colour,rules):
    # The colour we look for is specified by the variable 'bag_colour' on the first call
    bag_list = []
    for colour in rules:
        if rules[colour]==0:
            continue
        if bag_colour in rules[colour]: 
            bag_list.append(colour)
            bag_list += outer_bags(colour,rules)
    return bag_list

def inner_bags(bag_colour,rules):
    # The colour we look for is specified by the variable 'bag_colour' on the first call
    bag_num = 0
    if rules[bag_colour]==0:
        return 0
    for content in rules[bag_colour]:
        bag_num += rules[bag_colour][content]*(inner_bags(content,rules)+1)
    return bag_num

if __name__ == "__main__":
    print('Enter the name of the bag:')
    bag_colour = input()
    print('Enter the name of the filename:')
    filename = input()
    rules = rule_dict(filename)
    part_1 = len(set(outer_bags(bag_colour,rules)))
    part_2 = inner_bags(bag_colour,rules)
    print("\n")
    print(bag_colour.capitalize()+" bags are contained in {} other bags.".format(part_1))
    print("They must contain {} bags.".format(part_2)) 
