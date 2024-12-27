from dataclasses import dataclass
from abstract_advent_day import *
from data_reader import *
from util import *


@dataclass(slots=True, frozen=True)
class Data:
    instructions: str


@advent_info(day=1)
class AdventDay(AbstractAdventDay):
    def read(self, file_path: str) -> Data:
        return Data(read_full(file_path))

    @expected_answers(answer=280)
    def puzzle_1(self, data: Data) -> int:
        return data.instructions.count('(') - data.instructions.count(')')

    @expected_answers(example_answer=None, answer=None)
    def puzzle_2(self, data: Data) -> int:
        floor = 0

        for i, c in enumerate(data.instructions, start=1):
            if (floor := floor + (1 if c == '(' else -1)) < 0:
                return i
