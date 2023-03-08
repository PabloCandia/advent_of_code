import time

def read_file(filename):
    with open(filename, "r") as document:
        start_nums = document.readline().strip("\n").split(",")
    return [int(x) for x in start_nums]

def play(val, num_dict, n):
    for i in range(len(num_dict), n-1):
        if val not in num_dict:
            val2 = 0
            num_dict[val] = i
        if val in num_dict:
            val2 = i - num_dict[val]
            num_dict[val] = i
        val = val2
    return val

def run(filename, n):
    start_nums = read_file(filename)
    num_dict = {num: idx for idx, num in enumerate(start_nums[0:-1])}
    val = start_nums[-1]
    return play(val, num_dict, n)

if __name__ == "__main__":
    print("Enter the name of the input file:")
    filename = input()
    start = time.perf_counter()
    print("Part 1:", run(filename, 2020))
    print("Part 2:", run(filename, 30000000))
    end = time.perf_counter()
    print("{:.3f}".format((end-start)*1000))
