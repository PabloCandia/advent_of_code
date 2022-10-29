import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = [int(line.strip("\n")) for line in document]
    return doc

def is_valid(num, previous_list):
    for i in range(len(previous_list)):
        for j in range(i):
            if  previous_list[i] + previous_list[j] == num and previous_list[i] != previous_list[j]:
                return True
    return False

def find_invalid(num_list, n):
    for i in range(n, len(num_list)):
        if is_valid(num_list[i], num_list[i-n:i]) == False:
            return num_list[i]
    return 0

def find_summands(num_list, invalid_num):
    num_list.remove(invalid_num)
    for length in range(len(num_list)):
        for i in range(len(num_list)-length):
            lst = num_list[i:i+length]
            if sum(lst) == invalid_num:
                return lst
    return 0

def sum_max_min(num_list, n, invalid_num):
    summand_list = find_summands(num_list, invalid_num)
    return min(summand_list) + max(summand_list)

if __name__ == "__main__":
    start = time.perf_counter()
    document = read_file("input.txt")
    n = 25
    part_1 = find_invalid(document, n)
    part_2 = sum_max_min(document, n, part_1)
    print("Part 1: {}".format(part_1))
    print("Part 2: {}".format(part_2))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
