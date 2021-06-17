class Day10:
    known_arr_counts = {}

    def __init__(self):
        self.inputs = []
        with open("inputs/10.txt") as f:
            for line in f:
                self.inputs.append(int(line.strip()))
        self.inputs.sort()

    def part1(self):
        ones = 0
        threes = 0
        prev = 0
        for curr in self.inputs:
            if curr - prev == 1:
                ones += 1
            elif curr - prev == 3:
                threes += 1
            prev = curr

        return ones * (threes + 1)

    def part2(self):
        prev = 0
        for curr in self.inputs:
            if curr - prev == 1:

            elif curr - prev == 3:

            prev = curr
        return


problem = Day10()
print(problem.part1())
print(problem.part2())
