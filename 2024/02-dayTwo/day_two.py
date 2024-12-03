from itertools import pairwise

from utils.base_solution import BaseSolution

class Solution(BaseSolution):
    def format_input(self):
        rows = []
        lines = super().read_lines()
        for line in lines:
            rows.append([int(x) for x in line.split()])
        return rows

    def is_strictly_increasing(self, values: list[int]) -> bool:
        return all(x < y and 1 <= y - x <= 3 for x, y in pairwise(values))

    def is_safe(self, row: list[int]) -> bool:
        return self.is_strictly_increasing(row) or self.is_strictly_increasing(row[::-1]) # reversed

    def omit_one(self, values: list[int]):
        for idx in range(len(values)):
            yield values[:idx] + values[idx + 1 :]

    def solution1(self):
        formatted_input = self.format_input()
        res = sum(self.is_safe(report) for report in formatted_input)
        return res

    def solution2(self):

        formatted_input = self.format_input()
        res = sum(self.is_safe(report) or any(self.is_safe(i) for i in self.omit_one(report)) for report in formatted_input)
        return res