import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = [[pos for pos in line.strip("\n")] for line in document]
    return doc

class Layout:
    def __init__(self, arr, part):
        self.layout = arr
        self.new_layout = [["." for seat in row] for row in self.layout]
        self.dir_dict = {"NW": (-1, -1), "N": (-1, 0), "NE": (-1, 1), "W": (0, -1),
                        "E": (0, 1), "SW": (1, -1), "S": (1, 0), "SE": (1, 1)}
        self.update_layout(part)

    def is_stable(self):
        if self.layout == self.new_layout:
            return True
        else:
            return False

    def count_occupied_seats(self):
        return sum([row.count("#") for row in self.layout])

    def get_visible_seats(self, i, j, part):
        occ_seats = 0
        i_max, j_max = (len(self.layout), len(self.layout[0]))
        for dir in ["NW", "N", "NE", "W", "E", "SW", "S", "SE"]:
            i_dir, j_dir = (i + self.dir_dict[dir][0], j + self.dir_dict[dir][1])
            while 0 <= i_dir < i_max and 0 <= j_dir < j_max:
                if self.layout[i_dir][j_dir] == "L":
                    break
                if self.layout[i_dir][j_dir] == "#":
                    occ_seats += 1
                    break
                if part == 1:
                    break
                i_dir, j_dir = (i_dir + self.dir_dict[dir][0], j_dir + self.dir_dict[dir][1])
            if occ_seats >= part + 3:
                break
        return occ_seats

    def change_seat_state(self, i, j, part):
        occ_seats = self.get_visible_seats(i, j, part)
        seat = self.layout[i][j]
        if seat == "L" and occ_seats == 0:
            return "#"
        if seat == "#" and occ_seats >= part + 3:
            return "L"
        else:
            return seat

    def update_layout(self, part):
        for i in range(0, len(self.layout)):
            for j in range(0, len(self.layout[0])):
                if self.layout[i][j] == ".":
                    self.new_layout[i][j] = "."
                else:
                    self.new_layout[i][j] = self.change_seat_state(i, j, part)

    def refresh(self, part):
        self.layout = [row[:] for row in self.new_layout]
        self.update_layout(part)

def run(filename, part):
    document = read_file(filename)
    seats = Layout(document, part)
    if part == 1:
        while not seats.is_stable():
            seats.refresh(1)
        return seats.count_occupied_seats()
    if part == 2:
        while not seats.is_stable():
            seats.refresh(2)
        return seats.count_occupied_seats()

if __name__ == "__main__":
    print("Enter the name of the input file:")
    filename = input()
    start = time.perf_counter()
    print("Part 1:", run(filename, 1))
    print("Part 2:", run(filename, 2))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
