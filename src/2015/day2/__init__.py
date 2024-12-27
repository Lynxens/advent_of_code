from dataclasses import dataclass
from functools import reduce
from itertools import combinations, pairwise
from operator import mul

from abstract_advent_day import *
from data_reader import *
from util import *


@dataclass(slots=True, frozen=True)
class Data:
    present_dimensions: list[tuple[int, int, int]]


@advent_info(day=2)
class AdventDay(AbstractAdventDay):
    def read(self, file_path: str) -> Data:
        return Data([
            split_twice(line, 'x', int) for line in read_lines(file_path)
        ])

    @expected_answers(example_answer=101, answer=1588178)
    def puzzle_1(self, data: Data) -> int:
        return sum(
            2 * sum(sides) + min(sides)
            for sides in map(lambda d: (d[0] * d[1], d[1] * d[2], d[2] * d[0]), data.present_dimensions)
        )

    @expected_answers(example_answer=48, answer=3783758)
    def puzzle_2(self, data: Data) -> int:
        return sum(
            2 * (d[0] + d[1]) + reduce(mul, d)
            for d in map(sorted, data.present_dimensions)
        )
