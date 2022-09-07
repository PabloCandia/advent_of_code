def read_file(filename):
    with open(filename, "r") as document:
        doc = [line.strip("\n") for line in document]
    return doc

def partition(tup, char):
    if char == "B" or char == "R":
        return ((tup[1]+tup[0]+1)/2, tup[1])
    if char == "F" or char == "L":
        return (tup[0], (tup[1]+tup[0]-1)/2)

def get_seat(row_binary, col_binary):
    tup_row = (0, 127)
    tup_col = (0,7)
    for char in row_binary:
        tup_row = partition(tup_row, char)
    for char in col_binary:
        tup_col = partition(tup_col, char)
    return tup_row[0], tup_col[0]

def get_id(row, col):
    return int(8*row + col)

def part_1(filename):
    seat_list = read_file(filename)
    id_list = []
    for seat in seat_list:
        row_binary, col_binary = seat[:7], seat[7:]
        row, col = get_seat(row_binary, col_binary)
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
