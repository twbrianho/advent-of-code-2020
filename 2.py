class Day2:
    def __init__(self):
        self.inputs = []
        with open("inputs/2.txt") as f:
            for line in f:
                elements = line.strip().split()
                min, max = elements[0].split("-")
                target = elements[1][0]
                row = {
                    "min": int(min),
                    "max": int(max),
                    "target": target,
                    "pw": elements[2],
                }
                self.inputs.append(row)

    def part1(self):
        ans = 0
        for input in self.inputs:
            count = 0
            for c in input["pw"]:
                if c == input["target"]:
                    count += 1
            if input["min"] <= count <= input["max"]:
                ans += 1
        return ans

    def part2(self):
        ans = 0
        for input in self.inputs:
            if (input["pw"][input["min"] - 1] == input["target"]) != (input["pw"][input["max"] - 1] == input["target"]):
                ans += 1
        return ans


problem = Day2()
print(problem.part1())
print(problem.part2())
