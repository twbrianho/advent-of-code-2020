from functools import reduce


class Day3:
    TREE = "#"

    def __init__(self):
        self.inputs = []
        with open("inputs/3.txt") as f:
            for line in f:
                self.inputs.append(str(line.strip()))

    def traverse(self, dx: int, dy: int = 1):
        count = 0
        x, y = 0, 0
        while y < len(self.inputs):
            row = self.inputs[y]
            if row[x % len(row)] == self.TREE:
                count += 1
            x += dx
            y += dy

        return count

    def part1(self):
        return self.traverse(3)

    def part2(self):
        counts = [
            self.traverse(dx=1, dy=1),
            self.traverse(dx=3, dy=1),
            self.traverse(dx=4, dy=1),
            self.traverse(dx=7, dy=1),
            self.traverse(dx=1, dy=2),
        ]
        return reduce(lambda x, y: x * y, counts)


problem = Day3()
print(problem.part1())
print(problem.part2())
