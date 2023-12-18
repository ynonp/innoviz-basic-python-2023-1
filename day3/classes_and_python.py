class Summer():
    total = 0
    def add(self, value):
        self.total += value

    def __str__(self):
        return f"Summer [{self.total}]"

    def __add__(self, other):
        self.total += other
        return self


s = Summer()
s.add(10)
s.add(20)

s += 50
s.add(20)

print(s)






