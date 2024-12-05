import math
from itertools import product

from utils.base_solution import BaseSolution


class Solution(BaseSolution):
    rules = []
    updates = []

    def format_input(self):
        is_rule = True
        for line in super().read_lines():
            if line == "":
                is_rule = False
                continue

            if is_rule:
                self.rules.append(line)
            else:
                self.updates.append(line)
        return


    def is_correct_order(self, page_0: int, page_1: int):
        for rule in self.rules:
            page_before = int(rule.split('|')[0])
            page_after = int(rule.split('|')[1])
            if page_after == page_0 and page_before == page_1:
                return False
        return True

    def is_update_correct(self, update: str):
        pages = update.split(',')
        for i, j in [(i, j) for i in range(len(pages)) for j in range(i + 1, len(pages))]:

            if not self.is_correct_order(int(pages[i]), int(pages[j])):
                return 0

        mid = math.ceil(len(pages) / 2)
        return int(pages[mid - 1])

    def swap(self, pages: list[int], x: int, y: int):
        a = pages[x]
        pages[x] = pages[y]
        pages[y] = a

    def correct_updates(self, update):
        pages = [int(x) for x in update.split(',')]
        for i, j in [(i, j) for i in range(len(pages)) for j in range(i + 1, len(pages))]:
            for rule_idx in range(len(self.rules)):
                page_before = int(self.rules[rule_idx].split('|')[0])
                page_after = int(self.rules[rule_idx].split('|')[1])
                if page_after == pages[i] and page_before == pages[j]:
                    self.swap(pages, i, j)
                    rule_idx = 0

        mid = math.ceil(len(pages) / 2)
        return int(pages[mid - 1])

    def solution1(self):
        res = 0
        self.format_input()
        for update in self.updates:
            pages = [int(x) for x in update.split(',')]
            res += self.is_update_correct(update)

        return res

    def solution2(self):
        self.format_input()
        res = 0
        for update in self.updates:
            if not self.is_update_correct(update) == 0:
                continue
            res += self.correct_updates(update)
        return res
