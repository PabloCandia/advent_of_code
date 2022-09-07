def read_file(filename):
    with open(filename, "r") as document:
        doc = [line.strip("\n") for line in document]
    return doc

def binary_to_decimal(binary):
    decimal = 0
    for char in binary:
        if char == "F" or char == "L":
            decimal = decimal*2 + 0
        if char == "B" or char == "R":
            decimal = decimal*2 + 1
    return decimal

def get_id(row, col):
    return int(8*row + col)

def part_1(filename):
    seat_list = read_file(filename)
    id_list = []
    for seat in seat_list:
        row, col = binary_to_decimal(seat[:7]), binary_to_decimal(seat[7:])
        id_list.append(get_id(row, col))
    return id_list

def part_2(filename):
    id_list = part_1(filename)
    id_list.sort()
    c = id_list[0]
    for id_ in id_list:
        if c != id_:
            return c
        c+=1

if __name__ == "__main__":
    print("Enter the name of the file:")
    filename = input()
    print("The highest seat ID o a boarding pass is " + str(max(part_1(filename))))
    print("Your seat ID has to be " + str(part_2(filename)))
