# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import dataclasses
from dataclasses import dataclass

@dataclass
class TestDto:
    _name: str
    count: int
    status: str = 'PENDING'

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name


if __name__ == "__main__":
    dto = TestDto('name', 213)
    dto.name = 'aa'
    print(vars(dto))
    print(dataclasses.asdict(dto))
