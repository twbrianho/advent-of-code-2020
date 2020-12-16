class Day9:
    def __init__(self):
        self.inputs = []
        with open("inputs/9.txt") as f:
            for line in f:
                self.inputs.append(int(line.strip()))

    def part1(self):
        i = 25
        while i < len(self.inputs):
            curr_num = self.inputs[i]
            preamble = self.inputs[i - 25:i]
            no_sum = True
            for pre_num in preamble:
                if curr_num - pre_num in preamble:
                    no_sum = False
                    break
            if no_sum:
                return curr_num
            i += 1
        return "No answer"

    def part2(self):
        target = self.part1()
        start = 0
        end = 0
        curr_total = 0
        while curr_total != target:
            curr_total = sum(self.inputs[start: end])
            if curr_total < target:
                end += 1
                curr_total += self.inputs[end]
            else:
                curr_total -= self.inputs[start]
                start += 1

        return min(self.inputs[start: end]) + max(self.inputs[start: end])


problem = Day9()
print(problem.part1())
print(problem.part2())
