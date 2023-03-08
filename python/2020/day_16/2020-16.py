import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = [x.strip("\n") for x in document]
    return doc

def get_values(rule):
    field, ranges = rule.split(":")
    interval_1, interval_2 = ranges.split(" or ")
    val_set = set() # We store all the possible values a field can take in a set
    for interval in [interval_1, interval_2]:
        lower, upper = interval.split("-")
        val_set.update(list(range(int(lower), int(upper)+1))) # We use update to add list to sets
    return field, val_set

def make_rule_dict(rule_lst):
    rule_dict = {}
    for rule in rule_lst:
        field, val_set = get_values(rule)
        rule_dict[field] = val_set
    return rule_dict

def convert_int(lst):
    return [int(x) for x in lst]

def make_tkt_lst(tkt_lst):
    nested_lst = [convert_int(tkt.split(",")) for tkt in tkt_lst]
    return nested_lst

def parse_input(filename):
    doc = read_file(filename)
    my_idx, near_idx = doc.index("your ticket:"), doc.index("nearby tickets:")
    rule_lst = [doc[i] for i in range(my_idx)[:-1]]
    tkt_lst = make_tkt_lst(doc[near_idx + 1:])
    my_tkt = [int(x) for x in doc[my_idx + 1].split(",")]
    rule_dict = make_rule_dict(rule_lst)
    return rule_dict, my_tkt, tkt_lst

def make_field_dict(rule_dict, valid_lst):
    field_dict = {}
    for i in range(len(valid_lst[0])):
        field_lst = []
        for rule in rule_dict:
            acc = 1
            for j in range(len(valid_lst)):
                if valid_lst[j][i] not in rule_dict[rule]:
                    acc = 0
                    break
            if acc == 1:
                field_lst.append(rule)
        field_dict[i] = field_lst
    return field_dict

def reduce_fields(field_dict):
    n = 0
    keys = list(field_dict.keys())
    while n < len(field_dict):
        for i, key in enumerate(keys):
            if len(field_dict[key]) == 1:
                remove_field = field_dict[key][0]
                keys.pop(i)
        for i, key in enumerate(keys):
            if remove_field in field_dict[key]:
                field_dict[key].remove(remove_field)
        n += 1
    return [x[0] for x in field_dict.values()]

def mult_tkt_entries(field_lst, my_tkt):
    acc = 1
    names = ["departure location", "departure station", "departure platform",
             "departure track", "departure date", "departure time"]
    for i, field in enumerate(field_lst):
        if field in names:
            acc *= my_tkt[i]
    return acc

def part_1(filename):
    rule_dict, _, tkt_lst = parse_input(filename)
    full_set = set()
    for key in rule_dict.keys():
        full_set.update(rule_dict[key])
    error_rate = 0
    invalid_lst = []
    for i, tkt in enumerate(tkt_lst):
        for field_val in tkt:
            if field_val not in full_set:
                error_rate += field_val
                invalid_lst.append(i)
    return error_rate, invalid_lst

def part_2(filename, invalid_lst):
    rule_dict, my_tkt, tkt_lst = parse_input(filename)
    valid_lst = [tkt for i, tkt in enumerate(tkt_lst) if i not in invalid_lst]
    field_dict = make_field_dict(rule_dict, valid_lst)
    field_lst = reduce_fields(field_dict)
    return mult_tkt_entries(field_lst, my_tkt)

if __name__ == "__main__":
    filename = input("Enter the name of the input file: ")
    start = time.perf_counter()
    ans1, invalid_lst = part_1(filename)
    print("Part 1:", ans1)
    print("Part 2:", part_2(filename, invalid_lst))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
