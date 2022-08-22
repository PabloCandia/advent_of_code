def count_trees(filename, start_point, right, down):
    c = 0
    with open(filename,"r") as document:
        docu_list = list(document)
        len_str = len(docu_list[0])-1
        for i in range((len(docu_list))//down+(len(docu_list))%down):
            if docu_list[down*i][(start_point+i*right)%len_str]=="#":
                c += 1
        return c    

if __name__ == "__main__":
    print("Enter filename:")
    filename = input()
    print("The answer to part one is "+str(count_trees(filename,0,3,1))+" trees.")
    instructions = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    product = eval("*".join([str(count_trees(filename,0,instruction[0],instruction[1])) for instruction in instructions]))
    print("The answer to part two is "+str(product)+".")
