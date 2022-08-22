def parse_policy(policy):
    interval, character = policy.split(" ")
    lower_limit, upper_limit = interval.split("-")
    return int(lower_limit), int(upper_limit), character

def is_valid(password, parsed_policy, part):
    lower_limit, upper_limit, character = parsed_policy
    if part=='1':
        return lower_limit<=password.count(character) and password.count(character)<=upper_limit
    elif part=='2':
        return (password[lower_limit-1]==character) ^ (password[upper_limit-1]==character)
    else:
        print("Invalid input for 'part'.")
        
def count_valid_passwords(filename, part):
    c = 0
    with open(filename, "r") as document:
        for line in document:
            policy, password = line.split(": ")
            if is_valid(password, parse_policy(policy), part)==True:
                c += 1
        return c

if __name__ == "__main__":
    print("Enter the name of the file with policies and passwords:")
    filename = input()
    print("Which part of the puzzle is it? Enter 1 or 2.")
    part = input()
    print("Following the rules of part "+part+", there are {} valid passwords in the file.".format(count_valid_passwords(filename, part)))
