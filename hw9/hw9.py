# 99
k = int(input())
n = int(input())

page = (n - 1) // k + 1
line = (n - 1) % k + 1

print(page, line)

# 177
n = int(input())

s = f"{n:04d}"

if len(set(s)) == 4:
    print(True)
else:
    print(False)

# 291
n = int(input())

while n > 0:
    print(n % 10, end="")
    n //= 10

# 818
class MoneyBox:
    def __init__(self, capacity):
        self.capacity = capacity
        self.coins = 0

    def can_add(self, v):
        return self.coins + v <= self.capacity

    def add(self, v):
        self.coins += v


n = int(input())
m = int(input())
k = int(input())

box = MoneyBox(n)
box.add(m)
print(box.can_add(k))

# 820
class Buffer:
    def __init__(self):
        self.data = []

    def add(self, *a):
        self.data.extend(a)
        while len(self.data) >= 5:
            print(sum(self.data[:5]))
            self.data = self.data[5:]

    def get_current_part(self):
        return self.data


buffer = Buffer()

while True:
    try:
        nums = list(map(int, input().split()))
        buffer.add(*nums)
        print(buffer.get_current_part())
    except EOFError:
        break