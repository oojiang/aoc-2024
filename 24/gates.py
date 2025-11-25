class Gate:
    gates = {}

    def __init__(self, name: str):
        self.name = name
        Gate.gates[name] = self

    def compute(self):
        raise NotImplementedError()

class Input(Gate):
    def __init__(self, name: str, value: int):
        super().__init__(name)
        self.value = value

    def compute(self):
        return self.value

class Branch(Gate):
    def __init__(self, name: str, left: str, right: str):
        super().__init__(name)
        self.left = left
        self.right = right
        self.computed = False

class And(Branch):
    def compute(self):
        if self.computed:
            return self.value
        left_val = Gate.gates[self.left].compute()
        right_val = Gate.gates[self.right].compute()
        self.computed = True
        self.value = left_val and right_val
        return self.value

class Or(Branch):
    def compute(self):
        if self.computed:
            return self.value
        left_val = Gate.gates[self.left].compute()
        right_val = Gate.gates[self.right].compute()
        self.computed = True
        self.value = left_val or right_val
        return self.value

class Xor(Branch):
    def compute(self):
        if self.computed:
            return self.value
        left_val = Gate.gates[self.left].compute()
        right_val = Gate.gates[self.right].compute()
        self.computed = True
        self.value = int((left_val and not right_val) or (not left_val and right_val))
        return self.value
