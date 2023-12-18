class Summer:
    total: int = 0

    def add(self, *value: int):
        self.total += sum(value)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
print(s.total)

# should print 50
print(t.total)