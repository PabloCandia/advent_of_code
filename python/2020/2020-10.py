import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = [int(line.strip("\n")) for line in document]
    return doc

def gap_counts(document):
    document.sort()
    adapter_list = [0] + document
    gap_dict = {"+1": 0, "+2": 0, "+3": 0}
    for i in range(len(adapter_list))[1:]:
        if adapter_list[i]-adapter_list[i-1] == 1:
            gap_dict["+1"]+=1
        if adapter_list[i]-adapter_list[i-1] == 2:
            gap_dict["+2"]+=1
        if adapter_list[i]-adapter_list[i-1] == 3:
            gap_dict["+3"]+=1
    gap_dict["+3"]+=1
    return gap_dict

def count_combinations(jolt_list):
    combination_dict = {jolt: 0 for jolt in jolt_list}
    combination_dict[0] = 1
    for jolt in jolt_list:
        for j in range(3):
            if jolt + j + 1 in jolt_list:
                combination_dict[jolt + j + 1] += combination_dict[jolt]
    return combination_dict[jolt_list[-1]]

def part_1(document):
    gap_dict = gap_counts(document)
    return gap_dict["+1"]*gap_dict["+3"]

def part_2(document):
    document.sort()
    jolt_list = [0] + document + [document[-1] + 3]
    return count_combinations(jolt_list)

if __name__ == "__main__":
    print("Enter the filename:")
    filename = input()
    start = time.perf_counter()
    document = read_file(filename)
    print("Part 1: ", part_1(document))
    print("Part 2: ", part_2(document))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
