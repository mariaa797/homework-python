from typing import Protocol


# 1. Протокол
class Drawable(Protocol):
    def draw(self) -> str:
        ...


# 2. Функція render
def render(shape: Drawable) -> None:
    print(shape.draw())


# 3. Класи, що структурно відповідають Drawable
class Circle:
    def draw(self) -> str:
        return "( )"


class Square:
    def draw(self) -> str:
        return "[ ]"


# 4. Перевірка
render(Circle())
render(Square())