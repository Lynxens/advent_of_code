from dataclasses import dataclass
from dis import Instruction

import numpy as np

from abstract_advent_day import *
from data_reader import *
from util import *
import re


@dataclass(slots=True, frozen=True)
class Instruction:
    command: str
    start: tuple[int, int]
    end: tuple[int, int]

@dataclass(slots=True, frozen=True)
class Data:
    instructions: list[Instruction]


@advent_info(day=6)
class AdventDay(AbstractAdventDay):
    def read(self, file_path: str) -> Data:
        regex = re.compile(r"(?P<command>turn on|turn off|toggle) (?P<start>\d+,\d+) through (?P<end>\d+,\d+)")

        instructions = []
        for match in regex.finditer(read_full(file_path)):
            command, start, end = match.groups()
            start_y, start_x = split_once(start, ',', int)
            end_y, end_x = split_once(end, ',', int)

            instructions.append(Instruction(
                command,
                (start_y, start_x),
                (end_y, end_x),
            ))

        return Data(instructions)

    @expected_answers(example_answer=998996, answer=569999)
    def puzzle_1(self, data: Data) -> int:
        grid = np.zeros((1000, 1000), dtype=bool)

        for instruction in data.instructions:
            start_y, start_x = instruction.start
            end_y, end_x = instruction.end

            match instruction.command:
                case 'turn on':
                    grid[start_y:(end_y + 1), start_x:(end_x + 1)] = True
                case 'turn off':
                    grid[start_y:(end_y + 1), start_x:(end_x + 1)] = False
                case 'toggle':
                    grid[start_y:(end_y + 1), start_x:(end_x + 1)] = np.logical_not(grid[start_y:(end_y + 1), start_x:(end_x + 1)])

        return np.sum(grid)

    @expected_answers(example_answer=1001996, answer=17836115)
    def puzzle_2(self, data: Data) -> int:
        grid = np.zeros((1000, 1000), dtype=np.int64)

        for instruction in data.instructions:
            start_y, start_x = instruction.start
            end_y, end_x = instruction.end

            match instruction.command:
                case 'turn on':
                    grid[start_y:(end_y + 1), start_x:(end_x + 1)] += 1
                case 'turn off':
                    grid[start_y:(end_y + 1), start_x:(end_x + 1)] -= 1
                    grid[grid < 0] = 0
                case 'toggle':
                    grid[start_y:(end_y + 1), start_x:(end_x + 1)] += 2

        return np.sum(grid)
