def parse_line(line):
    policy, password = line.split(": ")
    interval, char = policy.split(" ")
    lower_lim, upper_lim = interval.split("-")
    return int(lower_lim), int(upper_lim), char, password

def is_valid(line, part):
    lower_lim, upper_lim, char, password = parse_line(line)
    count_char = password.count(char)
    if part=='1':
        return lower_lim <= count_char <= upper_lim
    elif part=='2':
        return (password[lower_lim-1]==char) ^ (password[upper_lim-1]==char)
    else:
        print("Invalid input for 'part'.")
        
def count_valid_passwords(filename, part):
    c = 0
    with open(filename, "r") as document:
        for line in document:
            if is_valid(line, part)==True:
                c += 1
        return c

if __name__ == "__main__":
    print("Enter the name of the file with policies and passwords:")
    filename = input()
    print("Which part of the puzzle is it? Enter 1 or 2.")
    part = input()
    print("Following the rules of part "+part+", there are {} valid passwords in the file.".format(count_valid_passwords(filename, part)))
