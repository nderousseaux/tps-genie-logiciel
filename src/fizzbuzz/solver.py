from fizzbuzz import FizzBuzz


class Displayer:
    def display(self, s):
        pass


class MyDisplayer(Displayer):
    def display(self, s):
        print(s)


class Int2String:
    def convert(self, s):
        pass


class MyConvertor(Int2String):
    def convert(self, s):
        return s.toString()


class ProblemSolver:
    def __init__(self, Int2String, displayer):
        self.displayer = displayer
        self.converter = Int2String

    def solve(self):
        for i in range(0, 100):
            self.displayer.display((self.converter.convert(i)))


if __name__ == "__main__":
    solver = ProblemSolver(FizzBuzz(), MyDisplayer())
    solver.solve()
