from dataclasses import dataclass
import numpy as np

from abstract_advent_day import *
from data_reader import *
from util import *


@dataclass(slots=True, frozen=True)
class Data:
    directions: np.ndarray


@advent_info(day=3)
class AdventDay(AbstractAdventDay):
    def read(self, file_path: str) -> Data:
        dydx = {
            '^': [-1, 0],
            '>': [0, 1],
            'v': [1, 0],
            '<': [0, -1],
        }

        return Data(np.array([*map(dydx.get, read_full(file_path))]))

    @expected_answers(example_answer=2, answer=2572)
    def puzzle_1(self, data: Data) -> int:
        return np.unique(directions_to_coords(data.directions), axis=0).shape[0]

    @expected_answers(example_answer=11, answer=2631)
    def puzzle_2(self, data: Data) -> int:
        return np.unique(np.vstack([
            directions_to_coords(data.directions[0::2]),
            directions_to_coords(data.directions[1::2]),
        ]), axis=0).shape[0]


def directions_to_coords(directions: np.ndarray) -> np.ndarray:
    return np.cumsum(np.vstack([[0, 0], directions]), axis=0)
