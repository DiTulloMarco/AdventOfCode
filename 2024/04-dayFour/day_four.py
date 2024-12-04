import itertools

from utils.base_solution import BaseSolution

class Solution(BaseSolution):
    xmas = "XMAS"
    dirs = {
            "top-left": (-1, -1),
            "top": (0, -1),
            "top-right": (1, -1),
            "left": (-1, 0),
            "right": (1, 0),
            "bottom-left": (-1, 1),
            "bottom": (0, 1),
            "bottom-right": (1, 1)
        }

    def format_input(self):
        grid = []
        for line in super().read_lines():
            grid.append([c for c in line])
        return grid

    def is_xmas_aux(self, text: list[list[str]], pos: (int, int), step: int, direction: str) -> bool:
        if step == 4:
            return True
        if pos[0] < 0 or pos[1] < 0 or pos[1] >= len(text) or pos[0] >= len(text[pos[1]]):
            return False

        if text[pos[1]][pos[0]] != self.xmas[step]:
            return False

        return self.is_xmas_aux(text=text, pos=tuple(a + b for a, b in zip(pos, self.dirs[direction])),
                                step=step + 1, direction=direction)

    def is_xmas(self, text: list[list[str]], pos: (int, int)) -> int:
        return sum([self.is_xmas_aux(text=text, pos=tuple(a + b for a, b in zip(pos, self.dirs[direction])), step=1, direction=direction) for direction in self.dirs])


    def solution1(self):
        text = self.format_input()
        res = 0
        for y in range(len(text)):
            for x in range(len(text[y])):
                if text[y][x] == 'X':
                    res += self.is_xmas(text, (x, y))
        return res


    def solution2(self):
        text = self.format_input()
        words = ("MAS", "SAM")
        return sum(
            (
                    text[i - 1][j - 1] + text[i][j] + text[i + 1][j + 1] in words
                    and text[i - 1][j + 1] + text[i][j] + text[i + 1][j - 1] in words
            )
            for i, j in itertools.product(range(1, len(text) - 1), range(1, len(text[0]) - 1))
        )