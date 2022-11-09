import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = [x.strip("\n").split(",") for x in document]
    timestamp = int(doc[0][0])
    ids = [int(id) for id in doc[1] if id != "x"]
    idx = [i for i in range(len(doc[1])) if doc[1][i] != "x"]
    return timestamp, ids, idx

def list_min(lst):
    min_val = min(lst)
    min_index = lst.index(min_val)
    return min_val, min_index

def part_1(filename):
    timestamp, ids, _ = read_file(filename)
    minutes = [id - timestamp % id for id in ids]
    min_val, i_min = list_min(minutes)
    return ids[i_min]*minutes[i_min]

def list_mult(lst):
    m = 1
    for x in lst:
        m *= x
    return m

def extended_euclid(a_i, b_i): # Extended Euclid with back substitution
    if b_i == 0:
        return (a_i, 1, 0)
    gcd, x, y = extended_euclid(b_i, a_i % b_i)
    # To guess what to return, it's necesary to take Bezouts identity and evolve it one step
    return (gcd, y, x - (a_i//b_i)*y)

def modular_inverse(a, m):
    g, x, y = extended_euclid(a, m)
    if g != 1:
        raise Exception('No modular inverse for %i mod %i' % (a, m))
    else:
        return x % m

def part_2(filename):
    _, mods, idx = read_file(filename)
    m = list_mult(mods)
    a = [-i for i in idx]
    b = [m//mod for mod in mods]
    inv_b = [modular_inverse(b[i], mods[i]) for i in range(len(mods))]
    timestamp_sum = 0
    for i, mod in enumerate(mods):
        timestamp_sum += a[i]*b[i]*inv_b[i]
    return int(timestamp_sum) % m

if __name__ == "__main__":
    print("Enter the name of the input file:")
    filename = input()
    start = time.perf_counter()
    print("Part 1:", part_1(filename))
    print("Part 2:", part_2(filename))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*1000))
