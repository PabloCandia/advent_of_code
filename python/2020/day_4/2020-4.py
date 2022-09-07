def read_file(filename):
    with open(filename,"r") as document:
        str_acc = ""
        ppt_list = []
        for line in document:
            if line != "\n":
                str_acc+=line.strip("\n")+" "
                continue
            ppt_list.append(str_acc.strip(" "))
            str_acc = ""
        ppt_list.append(str_acc.strip(" "))
    return ppt_list

def fld_to_dict(ppt):
    fld_dict = {}
    flds = ppt.split(" ")
    for fld in flds:
        key, val = fld.split(":")
        fld_dict[key] = val
    return fld_dict

def ppt_dict(filename):
    ppt_list = read_file(filename)
    ppt_dict = {}
    for i, ppt in enumerate(ppt_list):
        ppt_dict["Passport "+str(i)] = fld_to_dict(ppt)
    return ppt_dict

def fld_val(ppt):
    flds = list(ppt.keys())
    return ("cid" in flds and len(flds) == 8) or ("cid" not in flds and len(flds) == 7)

def yr_val(ppt):
    ranges = {"byr": (1920, 2002), "iyr": (2010, 2020), "eyr": (2020, 2030)}
    c = 0
    for yr in val_rules:
        if len(ppt[yr]) == 4 and ranges[yr][0] <= int(ppt[yr]) <= ranges[yr][1]:
            c+=1
    return c == 3
        
def hgt_val(ppt):
    hgt = ppt["hgt"]
    if hgt[-2:] == "cm":
        return 150 <= int(hgt[0:-2]) <= 193
    elif hgt[-2:] == "in":
        return 59 <= int(hgt[0:-2]) <= 76
    else:
        return False
    
def hcl_val(ppt):
    hcl = ppt["hcl"]
    if hcl[0] == "#":
        if hcl[1:].isalnum() == True and len(hcl[1:]) == 6:
            return True
        else:
            return False
    return False

def ecl_val(ppt):
    if ppt["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
        return True
    return False

def pid_val(ppt):
    pid = ppt["pid"]
    if pid.isnumeric() == True and len(pid) == 9:
        return True
    return False
    
def part_1(filename):
    ppts = ppt_dict(filename)
    c = 0
    for key in ppts:
        ppt = ppts[key]
        if fld_val(ppt) == True:
            c+=1
    return c

def part_2(filename):
    ppts = ppt_dict(filename)
    c = 0
    for key in ppts:
        ppt = ppts[key]
        if fld_val(ppt) == True:
            if yr_val(ppt) == True and hgt_val(ppt) == True and hcl_val(ppt) == True and ecl_val(ppt) == True and pid_val(ppt) == True:
                c+=1
        else:
            continue
    return c
            
if __name__ == "__main__":
    print("Enter filename:")
    filename = input()
    print("For part 1, there are "+str(part_1(filename))+" valid passports.")
    print("For part 2, there are "+str(part_2(filename))+" valid passports.")
