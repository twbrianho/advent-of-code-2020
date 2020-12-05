def is_valid_byr(byr: str):
    return 1920 <= int(byr) <= 2002


def is_valid_iyr(iyr: str):
    return 2010 <= int(iyr) <= 2020


def is_valid_eyr(eyr: str):
    return 2020 <= int(eyr) <= 2030


def is_valid_hgt(hgt: str):
    num = int(hgt[:len(hgt) - 2])
    if hgt.endswith("cm"):
        return 150 <= num <= 193
    elif hgt.endswith("in"):
        return 59 <= num <= 76
    return False


def is_valid_hcl(hcl: str):
    if not len(hcl) == 7:
        return False
    if not hcl[0] == "#":
        return False
    if set(c for c in [hcl[1:]]).issubset(set([c for c in "0123456789abcdef"])):
        return False
    return True


def is_valid_ecl(ecl: str):
    if not len(ecl) == 3:
        return False
    if ecl not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
        return False
    return True


def is_valid_pid(pid: str):
    if not len(pid) == 9:
        return False
    return True


class Day4:
    # Only includes required fields (i.e. excludes cid)
    FIELD_TO_VALIDATOR_MAP = {
        "byr": is_valid_byr,
        "iyr": is_valid_iyr,
        "eyr": is_valid_eyr,
        "hgt": is_valid_hgt,
        "hcl": is_valid_hcl,
        "ecl": is_valid_ecl,
        "pid": is_valid_pid,
    }

    def __init__(self):
        self.inputs = []
        with open("inputs/4.txt") as f:
            curr_passport = {}
            for line in f:
                row = str(line.strip())
                if not row:
                    self.inputs.append(curr_passport)
                    curr_passport = {}
                    continue
                for field in row.split(" "):
                    k, v = field.split(":")
                    curr_passport[k] = v
            # Add final passport as well
            self.inputs.append(curr_passport)

    def part1(self):
        count = 0
        for passport in self.inputs:
            if self.is_valid_1(passport):
                count += 1
        return count

    def part2(self):
        count = 0
        for passport in self.inputs:
            if not self.is_valid_1(passport):
                continue
            if self.is_valid_2(passport):
                count += 1
        return count

    def is_valid_1(self, passport: dict):
        for field in self.FIELD_TO_VALIDATOR_MAP.keys():
            if not passport.get(field):
                return False
        return True

    def is_valid_2(self, passport: dict):
        for field, validator in self.FIELD_TO_VALIDATOR_MAP.items():
            value = passport.get(field)
            if not validator(value):
                return False
        return True


problem = Day4()
print(problem.part1())
print(problem.part2())
