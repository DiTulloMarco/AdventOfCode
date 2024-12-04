class BaseSolution:

    def read_input(self) -> str:
        """ Return a string with the 'input.txt' content """
        with open('input.txt') as f:
            return f.read()

    def read_lines(self) -> list[str]:
        """ Return a list of the lines in the file 'input.txt' """
        return self.read_input().splitlines()

    def read_first_line(self) -> str:
        """ Return a list of the lines in the file 'input.txt' """
        with open('input.txt') as f:
            return f.readline()