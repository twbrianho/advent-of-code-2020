class Day1:
    def __init__(self):
        self.inputs = []
        with open("inputs/1.txt") as f:
            for line in f:
                self.inputs.append(int(line.strip()))

    def part1(self):
        seen = set()
        for num in self.inputs:
            if (2020 - num) in seen:
                return (2020 - num) * num
            seen.add(num)
        print("No two numbers sum to 2020.")

    def part2(self):
        seen_nums = set()
        known_sums = {}  # sum of 2 numbers: what the 2 numbers are
        for num in self.inputs:
            known_sum_nums = known_sums.get(2020 - num)
            if known_sum_nums:
                return num * known_sum_nums[0] * known_sum_nums[1]
            seen_nums.add(num)
            for seen_num in seen_nums:
                known_sums[num + seen_num] = (num, seen_num)


problem = Day1()
print(problem.part1())
print(problem.part2())
