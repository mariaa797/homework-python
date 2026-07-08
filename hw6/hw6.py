class CandyStash:
    MAX_CAPACITY = 50

    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Кількість має бути невід'ємним цілим числом.")

    def __init__(self, count):
        self.validate_amount(count)
        self._count = min(count, self.MAX_CAPACITY)

    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)

    def __str__(self):
        return f"CandyStash ({self.count}/{self.MAX_CAPACITY})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        if isinstance(other, CandyStash):
            new_count = self.count + other.count
        else:
            new_count = self.count + other
        return CandyStash(min(new_count, self.MAX_CAPACITY))

    def __sub__(self, other):
        if isinstance(other, CandyStash):
            new_count = self.count - other.count
        else:
            new_count = self.count - other
        return CandyStash(max(new_count, 0))

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self.count == other.count
        if isinstance(other, int):
            return self.count == other
        return False