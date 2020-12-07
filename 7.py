import re


class ChildBag:
    def __init__(self, color: str, parent_color: str):
        self.color = color
        self.parent_colors = [parent_color]

    def __repr__(self):
        return f"({self.color}): {self.parent_colors}"

    def add_parent_color(self, parent_color: str):
        self.parent_colors.append(parent_color)


class ParentBag:
    def __init__(self, color: str, child_color: str, num_children: int):
        self.color = color
        self.child_colors = [(child_color, num_children)]

    def __repr__(self):
        return f"({self.color}): {self.child_colors}"

    def add_child_color(self, parent_color: str, num_children: int):
        self.child_colors.append((parent_color, num_children))


class Day7:
    parent_regex = re.compile(r"([ \w]+) bags")
    child_regex = re.compile(r"([\d]*) ?([ \w]+) bags?")

    def __init__(self):
        self.inputs = []
        with open("inputs/7.txt") as f:
            for line in f:
                self.inputs.append(str(line.strip()))

    def part1(self):
        # Parse input and build map
        color_to_bag_map = {}  # Color (str): Bag of that color (Bag)
        for row in self.inputs:
            parent_str, children_str = row.split("contain ")
            parent_color = re.match(self.parent_regex, parent_str).group(1)
            for child_str in children_str.split(", "):
                child_color = re.match(self.child_regex, child_str).group(2)
                if child_color == "no other":
                    continue
                bag = color_to_bag_map.get(child_color)
                if not bag:
                    color_to_bag_map[child_color] = ChildBag(child_color, parent_color)
                else:
                    color_to_bag_map[child_color].add_parent_color(parent_color)

        # Traverse tree and count set
        checked_colors = set()
        colors_to_check = {"shiny gold"}
        while colors_to_check:
            next_colors_to_check = set()
            for color_to_check in colors_to_check:
                bag = color_to_bag_map.get(color_to_check)
                if bag:
                    for parent_color in bag.parent_colors:
                        if parent_color in checked_colors:
                            continue
                        checked_colors.add(parent_color)
                        next_colors_to_check.add(parent_color)
            colors_to_check = next_colors_to_check

        return len(checked_colors)

    def part2(self):
        # Parse input and build map
        color_to_bag_map = {}  # Color (str): Bag of that color (Bag)
        for row in self.inputs:
            parent_str, children_str = row.split("contain ")
            parent_color = re.match(self.parent_regex, parent_str).group(1)
            for child_str in children_str.split(", "):
                child_color = re.match(self.child_regex, child_str).group(2)
                if child_color == "no other":
                    color_to_bag_map[parent_color] = None

                child_num = re.match(self.child_regex, child_str).group(1)
                if not child_num:
                    child_num = 0
                else:
                    child_num = int(child_num)

                bag = color_to_bag_map.get(parent_color)
                if not bag:
                    color_to_bag_map[parent_color] = ParentBag(parent_color, child_color, child_num)
                else:
                    color_to_bag_map[parent_color].add_child_color(child_color, child_num)

        # Traverse tree via recursion
        return self.get_num_bags(color_to_bag_map, "shiny gold")

    def get_num_bags(self, color_to_bag_map: dict, color: str):
        curr_bag = color_to_bag_map.get(color)
        if not curr_bag:
            return 1
        num = 0
        for child_color, count in curr_bag.child_colors:
            # The parent bags themselves also need ot be counted, hence the +1
            num += count * (self.get_num_bags(color_to_bag_map, child_color) + 1)
        return num


problem = Day7()
print(problem.part1())
print(problem.part2())
