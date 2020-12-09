class Instruction:
    def __init__(self, op: str, arg: int):
        self.op = op
        self.arg = arg

    def __repr__(self):
        return f"{self.op} {self.arg}"


class Day8:
    def __init__(self):
        self.inputs = []
        with open("inputs/8.txt") as f:
            for line in f:
                op, arg = str(line.strip()).split(" ")
                self.inputs.append(Instruction(op, int(arg)))

    def part1(self):
        accumulator = 0
        seen_line_nums = set()
        curr_line_num = 0

        while True:
            curr_line = self.inputs[curr_line_num]
            if curr_line.op == "acc":
                accumulator += curr_line.arg
                curr_line_num += 1
            elif curr_line.op == "jmp":
                curr_line_num += curr_line.arg
            else:
                curr_line_num += 1

            if curr_line_num in seen_line_nums:
                return accumulator

            seen_line_nums.add(curr_line_num)

    def try_parse(self, fixed_inputs):
        print(fixed_inputs)
        accumulator = 0
        seen_line_nums = set()
        curr_line_num = 0

        while curr_line_num < len(self.inputs):
            curr_line = fixed_inputs[curr_line_num]
            if curr_line.op == "acc":
                accumulator += curr_line.arg
                curr_line_num += 1
            elif curr_line.op == "jmp":
                curr_line_num += curr_line.arg
            else:
                curr_line_num += 1

            if curr_line_num in seen_line_nums:
                return False

            seen_line_nums.add(curr_line_num)

        return accumulator

    def part2(self):
        for i, instr in enumerate(self.inputs):
            if instr.op == "jmp":
                ans = self.try_parse(self.inputs[:i] + [Instruction("nop", instr.arg)] + self.inputs[i + 1:])
                if ans:
                    return ans
            elif instr.op == "nop":
                ans = self.try_parse(self.inputs[:i] + [Instruction("jmp", instr.arg)] + self.inputs[i + 1:])
                if ans:
                    return ans
        return "No answer found"


problem = Day8()
print(problem.part1())
print(problem.part2())
