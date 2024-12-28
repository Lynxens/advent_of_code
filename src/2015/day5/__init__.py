import re
from dataclasses import dataclass
from itertools import pairwise

from abstract_advent_day import *
from data_reader import *
from util import *
from more_itertools import windowed


@dataclass(slots=True, frozen=True)
class Data:
    strings: list[str]


@advent_info(day=5)
class AdventDay(AbstractAdventDay):
    def read(self, file_path: str) -> Data:
        return Data(read_lines(file_path))

    @expected_answers(example_answer=2, answer=255)
    def puzzle_1(self, data: Data) -> int:
        return len([*filter(
            lambda s:
                re.search(r'([aeiou].*){3,}', s) and
                not re.search(r'ab|cd|pq|xy', s) and
                any(a == b for a, b in pairwise(s)),
            data.strings,
        )])

    @expected_answers(example_answer=(2,), answer=55)
    def puzzle_2(self, data: Data) -> int:
        return len([*filter(
            lambda s:
                any(s.count(a + b) >= 2 for a, b in pairwise(s)) and
                any(a == c for a, _, c in windowed(s, n=3)),
            data.strings,
        )])
