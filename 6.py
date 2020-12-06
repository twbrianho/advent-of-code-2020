class Day6:
    def __init__(self):
        self.inputs = []
        with open("inputs/6.txt") as f:
            groups_raw = f.read().split("\n\n")
            self.inputs = [group_raw.split("\n") for group_raw in groups_raw]

    def part1(self):
        count = 0
        for group in self.inputs:
            group_set = set()
            for person in group:
                group_set.update(set(person))
            count += len(group_set)
        return count

    def part2(self):
        count = 0
        for group in self.inputs:
            group_set = set(group[0])
            for person in group[1:]:
                group_set = group_set.intersection(set(person))
            count += len(group_set)
        return count


problem = Day6()
print(problem.part1())
print(problem.part2())
