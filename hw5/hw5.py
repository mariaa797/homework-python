class Character:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self.max_hp = max_hp
        self.__hp = max_hp

    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, value):
        self.__hp = max(0, min(value, self.max_hp))

    def take_damage(self, amount: int) -> None:
        self.hp -= amount

    def heal(self, amount: int) -> None:
        self.hp += amount

    def is_alive(self) -> bool:
        return self.hp > 0