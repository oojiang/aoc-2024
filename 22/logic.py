class RNG:
    MOD_N = 16777216

    def __init__(self, secret):
        self.secret = secret
        self.evolutions = 0

    def mix(self, value):
        self.secret = self.secret ^ value

    def prune(self):
        self.secret = self.secret % RNG.MOD_N

    def step1(self):
        self.mix(self.secret * 64)
        self.prune()

    def step2(self):
        self.mix(self.secret // 32)
        self.prune()

    def step3(self):
        self.mix(self.secret * 2048)
        self.prune()

    def evolve(self):
        self.step1()
        self.step2()
        self.step3()
        self.evolutions += 1
        return self.secret
