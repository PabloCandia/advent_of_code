def read_file(filename):
    with open(filename,"r") as document:
        doc = [line.strip("\n") for line in document]
    return doc

def get_trajectory(start_point,step,len_chart):
    trajectory = [start_point]
    for coords in trajectory:
        if coords[1]+step[1] >= len_chart:
            break
        trajectory.append([coords[0]+step[0], coords[1]+step[1]])
    return trajectory
    
def count_trees(filename, start_point, step):
    chart = read_file(filename)
    return sum([int(chart[coord[1]][coord[0]%(len(chart[0]))]=="#") for coord in get_trajectory(start_point, step, len(chart))])

if __name__ == "__main__":
    print("Enter filename:")
    filename = input()
    print("The answer to part one is "+str(count_trees(filename, [0,0], [3,1]))+" trees.")
    instructions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    product = eval("*".join([str(count_trees(filename, [0,0], instruction)) for instruction in instructions]))
    print("The answer to part two is "+str(product)+".")
