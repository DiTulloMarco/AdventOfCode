from utils.base_solution import BaseSolution

class Solution(BaseSolution):
    left = []
    right = []
    def format_input(self):
        lines = super().read_lines()
        for line in lines:
            x, y = line.split()
            self.right.append(int(x))
            self.left.append(int(y))

        return zip(sorted(self.left), sorted(self.right))

    def solution1(self):
        formatted_input = self.format_input()
        res = sum(abs(x - y) for x, y in formatted_input)
        return res

    def solution2(self):
        formatted_input = self.format_input()
        res = 0
        for x, y in formatted_input:
            res += x * self.right.count(x)
        return res