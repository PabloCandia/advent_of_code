import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = document.read()
    return doc

class Grid_3D:
    def __init__(self, initial):
        self.grid = {}
        self.r_min = [0, 0, 0]
        self.r_max = [0, 0, 0]
        self.initial = initial
        self.start_grid()

    def start_grid(self):
        init_lst = self.initial.split("\n")[:-1]
        x_max, y_max = [len(init_lst), len(init_lst[0])]
        self.r_max = [x_max + 1, y_max + 1, 2]
        self.r_min = [-1, -1, -1]
        for i in range(x_max):
            for j in range(y_max):
                self.grid[(i, j, 0)] = init_lst[i][j]

    def near_count(self, x, y, z):
        acc = 0
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                for k in [z - 1, z, z + 1]:
                    if [i, j, k] == [x, y, z]:
                        continue
                    if (i, j, k) not in self.grid:
                        continue
                    if self.grid[(i, j, k)] == "#":
                        acc += 1
        return acc

    def fill_new_cells(self):
        for x in range(self.r_min[0], self.r_max[0]):
            for y in range(self.r_min[1], self.r_max[1]):
                for z in range(self.r_min[2], self.r_max[2]):
                    if (x, y, z) not in self.grid:
                        self.grid[(x, y, z)] = "."

    def extend_grid(self):
        for i in [0, 1, 2]:
            self.r_min[i] -= 1
            self.r_max[i] += 1

    def run_cycle(self):
        self.fill_new_cells()
        new_grid = {}
        for x in range(self.r_min[0], self.r_max[0]):
            for y in range(self.r_min[1], self.r_max[1]):
                for z in range(self.r_min[2], self.r_max[2]):
                    if self.grid[(x, y, z)] == "#":
                        if self.near_count(x, y, z) in [2, 3]:
                            new_grid[(x, y, z)] = "#"
                        else:
                            new_grid[(x, y, z)] = "."
                    if self.grid[(x, y, z)] == ".":
                        if self.near_count(x, y, z) == 3:
                            new_grid[(x, y, z)] = "#"
                        else:
                            new_grid[(x, y, z)] = "."
        self.grid = new_grid
        self.extend_grid()

    def evolve_grid(self, n):
        for i in range(n):
            self.run_cycle()

    def count_active(self):
        return sum([1 for i in self.grid.values() if i == "#"])

    def draw_grid_layer(self, z):
        for x in range(self.r_min[0]+1, self.r_max[0]-1):
            s = ""
            for y in range(self.r_min[1]+1, self.r_max[1]-1):
                s += self.grid[(x, y, z)]
            print(s)
        return 0

class Grid_4D:
    def __init__(self, initial):
        self.grid = {}
        self.r_min = [0, 0, 0, 0]
        self.r_max = [0, 0, 0, 0]
        self.initial = initial
        self.start_grid()

    def start_grid(self):
        init_lst = self.initial.split("\n")[:-1]
        x_max, y_max = [len(init_lst), len(init_lst[0])]
        self.r_max = [x_max + 1, y_max + 1, 2, 2]
        self.r_min = [-1, -1, -1, -1]
        for i in range(x_max):
            for j in range(y_max):
                self.grid[(i, j, 0, 0)] = init_lst[i][j]

    def near_count(self, x, y, z, w):
        acc = 0
        for i in [x - 1, x, x + 1]:
            for j in [y - 1, y, y + 1]:
                for k in [z - 1, z, z + 1]:
                    for l in [w - 1, w, w + 1]:
                        if [i, j, k, l] == [x, y, z, w]:
                            continue
                        if (i, j, k, l) not in self.grid:
                            continue
                        if self.grid[(i, j, k, l)] == "#":
                            acc += 1
        return acc

    def fill_new_cells(self):
        for x in range(self.r_min[0], self.r_max[0]):
            for y in range(self.r_min[1], self.r_max[1]):
                for z in range(self.r_min[2], self.r_max[2]):
                    for w in range(self.r_min[3], self.r_max[3]):
                        if (x, y, z, w) not in self.grid:
                            self.grid[(x, y, z, w)] = "."

    def extend_grid(self):
        for i in [0, 1, 2, 3]:
            self.r_min[i] -= 1
            self.r_max[i] += 1

    def run_cycle(self):
        self.fill_new_cells()
        new_grid = {}
        for x in range(self.r_min[0], self.r_max[0]):
            for y in range(self.r_min[1], self.r_max[1]):
                for z in range(self.r_min[2], self.r_max[2]):
                    for w in range(self.r_min[3], self.r_max[3]):
                        if self.grid[(x, y, z, w)] == "#":
                            if self.near_count(x, y, z, w) in [2, 3]:
                                new_grid[(x, y, z, w)] = "#"
                            else:
                                new_grid[(x, y, z, w)] = "."
                        if self.grid[(x, y, z, w)] == ".":
                            if self.near_count(x, y, z, w) == 3:
                                new_grid[(x, y, z, w)] = "#"
                            else:
                                new_grid[(x, y, z, w)] = "."
        self.grid = new_grid
        self.extend_grid()

    def evolve_grid(self, n):
        for i in range(n):
            self.run_cycle()

    def count_active(self):
        return sum([1 for i in self.grid.values() if i == "#"])

if __name__ == "__main__":
    filename = input("Enter the name of the input file: ")
    start = time.perf_counter()
    initial = read_file(filename)
    grid_1 = Grid_3D(initial)
    grid_1.evolve_grid(6)
    grid_2 = Grid_4D(initial)
    grid_2.evolve_grid(6)
    print("Part 1:", grid_1.count_active())
    print("Part 2:", grid_2.count_active())
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*100))
