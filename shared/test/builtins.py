from shared.test.config import Config
import traceback


def log(*args, **kwargs):
    if Config.VERBOSE:
        return print(*args, **kwargs)


class Test:
    def __init__(self, flhs=None, frhs=None):
        self.flhs = flhs
        self.frhs = frhs

    def fLHS(self):
        log(f"testing: {self.func.__qualname__}")

        def exec(lhs, rhs):
            try:
                flhs_lhs = self.flhs(*lhs)
                log(f"flhs_lhs = {flhs_lhs}")
                if Config.ASSERTION:
                    assert self.flhs(*lhs) == rhs
            except KeyError:
                if rhs == KeyError:
                    log("flhs correctly raised KeyError")
                else:
                    # print is here on purpose
                    print(f"function {self.func.__qualname__} incorrectly raised KeyError")
                    print(traceback.format_exc())
                    exit()

        def iter(res):
            for lhs, rhs in res:
                log(f"lhs: {lhs}")
                log(f"rhs: {rhs}")
                exec(lhs, rhs)
        iter(self.func())

    def __call__(self, func):
        self.func = func
        if self.flhs is not None and self.frhs is None:
            return self.fLHS
