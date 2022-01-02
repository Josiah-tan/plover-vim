from config import Global
from shared.test.config import Config


class Test:
    def __init__(self, mode=Config.TESTMODE, flhs=None, frhs=None):
        self.mode = mode
        self.flhs = flhs
        self.frhs = frhs

    def fLHS(self):
        if Config.VERBOSE:
            print(f"testing: {self.func.__qualname__}")

        def iter(res):
            for lhs, rhs in res:
                if Config.VERBOSE:
                    print(f"lhs: {lhs}")
                    print(f"rhs: {rhs}")
                    print(f"self.flhs(*lhs) = {self.flhs(*lhs)}")
                if Config.ASSERTION:
                    assert self.flhs(*lhs) == rhs
        res = self.func()
        if res is not None:
            iter(res)

    def __call__(self, func):
        self.func = func
        if self.mode == "fLHS":
            return self.fLHS
