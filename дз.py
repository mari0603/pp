class PowersOfTwo:
    def init(self):
        self.exp = 0
    def iter(self):
        return self
    def next(self):
        result = 2 ** self.exp
        self.exp += 1
        return result
powers = PowersOfTwo()
for _ in range(10):
    print(next(powers))
