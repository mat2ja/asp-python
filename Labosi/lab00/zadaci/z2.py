class Matematika():
    def __init__(self):
        self.a = 1

    def korijen(self, x):
        while abs(self.a ** 2 - x) > 0.001:
            self.a = (self.a + x / self.a) / 2
        return self.a

x = Matematika()
print(x.korijen(4))
print(x.korijen(25))
print(x.korijen(1024))