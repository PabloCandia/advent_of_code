import time

def memory_entry(line):
    mem, _, val = line.split(" ")
    rev_address = []
    for c in reversed(mem[0:-1]):
        if c != "[":
            rev_address.append(c)
        if c == "[":
            break
    address = [c for c in reversed(rev_address)]
    value = bin(int(val))
    return (int("".join(address)), "0"*(36 - len(value[2:])) + value[2:])

def parser(filename):
    with open(filename, "r") as document:
        doc = []
        for line in document:
            entry = line.strip("\n")
            if entry.split(" ")[0] == "mask":
                doc.append(("mask", entry.split(" ")[-1]))
            else:
                doc.append(memory_entry(entry))
        return doc

class Reader:
    def __init__(self, program):
        self.program = program
        self.mask = "X"*36
        self.memory_dict = {}

    def reset_dict(self):
        self.memory_dict = {}

    def dec_to_bin(self, decimal, num_zeroes = 36):
        binary = bin(int(decimal))
        return "0"*(num_zeroes - len(binary[2:])) + binary[2:]

    def mask_binary(self, binary):
        s = [c for c in binary]
        for i in range(len(self.mask)):
            if self.mask[i] != "X":
                s[i] = self.mask[i]
        return "".join(s)

    def fill_addresses(self, binary, value):
        s = [c for c in binary]
        for i in range(len(self.mask)):
            if self.mask[i] == "X":
                s[i] = self.mask[i]
            if self.mask[i] == "1":
                s[i] = self.mask[i]
        num_X = s.count("X")
        address_split = "".join(s).split("X")
        for i in range(2**num_X):
            address = ""
            replacements = self.dec_to_bin(i, num_X)
            for j in range(num_X):
                address += address_split[j] + replacements[j]
            address += address_split[-1]
            self.memory_dict[int(address, 2)] = int(value, 2)

    def decoder(self, entry):
        address, value = entry
        bin_address = self.dec_to_bin(address)
        self.fill_addresses(bin_address, value)

    def read_program(self, part):
        self.reset_dict()
        for entry in self.program:
            if entry[0] == "mask":
                self.mask = entry[1]
            else:
                if part == 1:
                    self.memory_dict[str(entry[0])] = int(self.mask_binary(entry[1]), 2)
                if part == 2:
                    self.decoder(entry)

def run(filename, part):
    program = parser(filename)
    reader = Reader(program)
    reader.read_program(part)
    return sum(reader.memory_dict.values())

if __name__ == "__main__":
    print("Enter the name of the input file:")
    filename = input()
    start = time.perf_counter()
    print("Part 1:", run(filename, 1))
    print("Part 2:", run(filename, 2))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
