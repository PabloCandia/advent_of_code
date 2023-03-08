import time

def read_file(filename):
    with open(filename, "r") as document:
        doc = [x.strip("\n") for x in document]
    return doc

def left_right_idx(str):
    acc = 0
    lst = []
    for i in range(len(str)):
        if str[i] == "(":
            acc += 1
            if acc == 1:
                lst.append(i)
        if str[i] == ")":
            acc -= 1
            if acc == 0:
                lst.append(i)
    return lst

def operate(expr1, expr2, operation):
    if operation == "+":
        return str(int(expr1) + int(expr2))
    if operation == "*":
        return str(int(expr1) * int(expr2))

def result(s):
    s_lst = s.split(" ")
    eval_lst = [c for c in s_lst if c != ""]
    if len(eval_lst) == 1:
        return eval_lst[0]
    while True:
        if len(eval_lst) == 3:
            eval_lst = [operate(eval_lst[0], eval_lst[2], eval_lst[1])]
            break
        eval_lst = [operate(eval_lst[0], eval_lst[2], eval_lst[1])] + eval_lst[3:]
    return eval_lst[0]

def result_adv(s):
    factor_lst = s.split("*")
    if len(factor_lst) == 1:
        return result(factor_lst[0])
    str_acc = "1"
    for factor in factor_lst:
        str_acc = str(int(result(factor))*int(str_acc))
    return str_acc

def replace_str(str, result_lst, idxs):
    new_str = ""
    range_lst = [-1] + idxs
    range_lst.append(len(str))
    for i in range(0, len(range_lst), 2):
        new_str += str[range_lst[i]+1:range_lst[i+1]]
        if i/2 < len(result_lst):
            new_str += result_lst[int(i/2)]
    return new_str

def eval_expr(str):
    if "(" not in str:
        return result(str)
    idxs = left_right_idx(str)
    result_lst = [eval_expr(str[idxs[i]+1:idxs[i+1]]) for i in range(0, len(idxs), 2)]
    new_str = replace_str(str, result_lst, idxs)
    return result(new_str)

def eval_expr_adv(str):
    if "(" not in str:
        return result_adv(str)
    idxs = left_right_idx(str)
    result_lst = [eval_expr_adv(str[idxs[i]+1:idxs[i+1]]) for i in range(0, len(idxs), 2)]
    new_str = replace_str(str, result_lst, idxs)
    return result_adv(new_str)

def part_1(filename):
    expr_lst = read_file(filename)
    return sum(int(eval_expr(expr)) for expr in expr_lst)

def part_2(filename):
    expr_lst = read_file(filename)
    return sum(int(eval_expr_adv(expr)) for expr in expr_lst)

if __name__ == "__main__":
    filename = input("Enter the name of the input file: ")
    start = time.perf_counter()
    print("Part 1:", part_1(filename))
    print("Part 2:", part_2(filename))
    end = time.perf_counter()
    print("{:.3f} ms".format((end-start)*100))
