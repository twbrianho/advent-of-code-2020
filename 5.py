class Day5:
    def __init__(self):
        self.inputs = []
        with open("inputs/5.txt") as f:
            for line in f:
                boarding_pass = str(line.strip())
                self.inputs.append(self.get_seat_id(boarding_pass))

    @staticmethod
    def get_seat_id(boarding_pass):
        bin_str = boarding_pass.replace("B", "1").replace("F", "0").replace("R", "1").replace("L", "0")
        return int(bin_str, 2)

    def part1(self):
        return max(self.inputs)

    def part2(self):
        missing_ids = set([i for i in range(1024)]) - set(self.inputs)

        # Note: missing_ids is sorted in ascending order, and definitely starts with 0
        prev_id = -1
        for curr_id in missing_ids:
            if curr_id != prev_id + 1:
                return curr_id
            prev_id = curr_id


problem = Day5()
print(problem.part1())
print(problem.part2())
