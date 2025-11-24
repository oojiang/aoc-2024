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

class Prices:
    def __init__(self, secret, n_changes = 2000):
        self.rng = RNG(secret)

        self.prices = [secret % 10]
        for _ in range(n_changes):
            self.prices.append(self.rng.evolve() % 10)

        self.deltas = [0]
        for i in range(1, len(self.prices)):
            self.deltas.append(self.prices[i] - self.prices[i - 1])

    def get_price(self, pattern):
        n = len(pattern)
        for i in range(n - 1, len(self.prices)):
            deltas = [self.deltas[i + m] for m in range(- n + 1, 1)]
            if deltas == pattern:
                return self.prices[i]
        return 0

    def pretty_print(self):
        for i in range(len(self.prices)):
            print(self.deltas[i], self.prices[i], sep='\t')
