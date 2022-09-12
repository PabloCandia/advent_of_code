import time

ACC = 0

def read_file(filename):
    with open(filename, "r") as document:
        return [[line[:3], int(line[3:])] for line in document]

def execute_instruction(instruction, line, nop_idx, jmp_idx):
    global ACC
    operation, argument = instruction
    if operation == "nop":
        nop_idx.append(line)
        return line + 1
    if operation == "acc":
        ACC =  ACC + argument
        return line + 1
    if operation == "jmp":
        jmp_idx.append(line)
        new_line = line + argument
        return new_line

def execute_loop(document, record, line, nop_idx, jmp_idx):
    line = execute_instruction(document[line], line, nop_idx, jmp_idx)
    if line >= len(document):
        return 1
    if line in record:
        return 0
    record.add(line)
    return execute_loop(document, record, line, nop_idx, jmp_idx)

def run_code(document):
    record = set()
    nop_idx = []
    jmp_idx = []
    return execute_loop(document, record, 0, nop_idx, jmp_idx), nop_idx, jmp_idx

def edit_code(document):
    global ACC
    _, nop_idx, jmp_idx = run_code(document)
    for nop in nop_idx:
        ACC = 0
        new_doc = [line[:] for line in document] # Attention to the deep copy of a list of lists!
        new_doc[nop][0] = "jmp"
        if run_code(new_doc)[0] == 1:
            return ACC
    for jmp in jmp_idx:
        ACC = 0
        new_doc = [line[:] for line in document]
        new_doc[jmp][0] = "nop"
        if run_code(new_doc)[0] == 1:
            return ACC

if __name__ == "__main__":
    start = time.perf_counter()
    document = read_file("example.txt")
    print(edit_code(document))
    end = time.perf_counter()
    print(f"{(end-start)*1000:.3f} ms")
