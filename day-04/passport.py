def validate(entry):
    if "byr" in entry and "iyr" in entry and "eyr" in entry and "hgt" in entry and "hcl" in entry and "ecl" in entry and "pid" in entry:
        # Part 2 checks
        if not 1920 <= int(entry["byr"]) <= 2002:
            return False
        
        if not 2010 <= int(entry["iyr"]) <= 2020:
            return False
        
        if not 2020 <= int(entry["eyr"]) <= 2030:
            return False
        
        if not (entry["hgt"][-2:] == "cm" or entry["hgt"][-2:] == "in"):
            return False

        if entry["hgt"][-2:] == "cm":
            if not 150 <= int(entry["hgt"][:-2]) <= 193:
                return False
        
        if entry["hgt"][-2:] == "in":
            if not 59 <= int(entry["hgt"][:-2]) <= 76:
                return False
        
        if entry["hcl"][0] == '#':
            for char in list(entry["hcl"][1:]):
                if char not in list("0123456789abcdef"):
                    return False
        else:
            return False
        
        if not entry["ecl"] in "amb blu brn gry grn hzl oth".split(" "):
            return False
        
        if not (len(entry["pid"]) == 9 and entry["pid"].isdecimal()):
            return False
        return True
    else:
        return False

def parse(entry_str):
    entry_str = entry_str.replace('\n', ' ')
    entries = entry_str.split(' ')
    passport_entry = {}
    for entry in entries:
        entry = entry.split(':')
        passport_entry[entry[0]] = entry[1]
    
    return passport_entry

def count_valid(entries):
    count = 0
    for entry in entries:
        if validate(entry):
            count += 1
    return count

def convert_file_to_entries(content):
    return content.split("\n\n")

def solve(content):
    entry_texts = convert_file_to_entries(content)
    entries = []
    for entry in entry_texts:
        entries.append(parse(entry))
    
    return count_valid(entries)


file = open("input.txt", "r")
content = file.read()
file.close()

print(solve(content))