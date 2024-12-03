from utils.base_solution import BaseSolution
import re

class Solution(BaseSolution):
    correct_form = r'mul\(\d{1,3},\d{1,3}\)'

    def format_input(self):
        return self.find_muls(super().read_input())

    def find_muls(self, text: str) -> list[str]:
        return re.findall(self.correct_form, text)

    def do_or_dont(self) -> list[str]:
        do = r'do\(\)'
        dont = r'don\'t\(\)'

        substring = ""
        for section in re.split(do, super().read_input()):
            x = re.search(dont, section)
            section = section if x is None else section[0:x.start()]
            substring += section

        return self.find_muls(substring)

    def get_operands(self, muls: list[str]):
        ops = []
        for operation in muls:
            ops.append([int(x) for x in operation[4:-1].split(',')])
        return ops

    def solution1(self):
        return sum(x * y for x, y in self.get_operands(self.format_input()))


    def solution2(self):
        return sum(x * y for x, y in self.get_operands(self.do_or_dont()))

print(Solution().solution1())
print(Solution().solution2())