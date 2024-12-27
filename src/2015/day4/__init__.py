from dataclasses import dataclass
from abstract_advent_day import *
from data_reader import *
from util import *
from hashlib import md5


@dataclass(slots=True, frozen=True)
class Data:
    key: str


@advent_info(day=5)
class AdventDay(AbstractAdventDay):
    def read(self, file_path: str) -> Data:
        return Data(read_full(file_path))

    @expected_answers(answer=117946)
    def puzzle_1(self, data: Data) -> int:
        i = 0
        while not md5(f'{data.key}{i}'.encode()).hexdigest().startswith('00000'):
            i += 1

        return i

    @expected_answers(answer=3938038)
    def puzzle_2(self, data: Data) -> int:
        i = 0

        while not md5(f'{data.key}{i}'.encode()).hexdigest().startswith('000000'):
            i += 1

        return i
