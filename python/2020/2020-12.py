import time

def parse_input(filename):
    with open(filename, "r") as document:
        doc = [line.strip("\n") for line in document]
        instructions = [(line[0], int(line[1:])) for line in doc]
    return instructions

class Trajectory:
    def __init__(self):
        self.initial_position = [0, 0]
        self.current_position = [0, 0]
        self.dir_dict = {"N": (0, 1), "W": (-1, 0), "E": (1, 0), "S": (0, -1)}
        self.waypoint = [0, 0]

    def set_waypoint(self, part):
        if part == 1:
            self.waypoint = [1, 0]
        if part == 2:
            self.waypoint = [10, 1]

    def abs(self, x):
        return (x**2)**0.5

    def manhattan_distance(self):
        x = self.abs(self.current_position[0] - self.initial_position[0])
        y = self.abs(self.current_position[1] - self.initial_position[1])
        return x + y

    def move(self, action, part):
        dir, step = action
        if dir in self.dir_dict:
            if part == 1:
                self.current_position[0] += step*self.dir_dict[dir][0]
                self.current_position[1] += step*self.dir_dict[dir][1]
            if part == 2:
                self.waypoint[0] += step*self.dir_dict[dir][0]
                self.waypoint[1] += step*self.dir_dict[dir][1]
        if dir == "F":
                self.current_position[0] += step*self.waypoint[0]
                self.current_position[1] += step*self.waypoint[1]

    def rotation(self, vec, angle):
        x, y = vec
        if angle == 90:
            return [-y, x]
        if angle == 180:
            return [-x, -y]
        if angle == 270:
            return [y, -x]

    def rotate(self, action):
        dir, angle = action
        if dir == "R":
            self.waypoint = self.rotation(self.waypoint, 360-angle)
        if dir == "L":
            self.waypoint = self.rotation(self.waypoint, angle)

    def update_position(self, instructions, part):
        self.set_waypoint(part)
        for action in instructions:
            if (action[0] == "R") or (action[0] == "L"):
                self.rotate(action)
            else:
                self.move(action, part)

def run(filename, part):
    instructions = parse_input(filename)
    trip = Trajectory()
    trip.update_position(instructions, part)
    return int(trip.manhattan_distance())

if __name__ == "__main__":
    print("Enter the name of the input file:")
    filename = input()
    start = time.perf_counter()
    print("Part 1:", run(filename, 1))
    print("Part 2:", run(filename, 2))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
