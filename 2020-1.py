def read_file(filename):
    with open(filename,'r') as file:
        numbers = [int(line) for line in file]
    return numbers

def multiply_right_pair(filename):
    numbers = read_file(filename)
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i]+numbers[j]==2020:
                return numbers[i]*numbers[j]
            
def multiply_right_triad(filename):
    numbers = read_file(filename)
    for i in range(len(numbers)):
        for j in range(i):
            for k in range(j):
                if numbers[i]+numbers[j]+numbers[k]==2020:
                    return numbers[i]*numbers[j]*numbers[k]

if __name__ == "__main__":
    print("Enter the filename:")
    filename = input()
    print("The product of the two entries that add to 2020 is {}".format(multiply_right_pair(filename)))
    print("The product of the three entries that add to 2020 is {}".format(multiply_right_triad(filename)))
