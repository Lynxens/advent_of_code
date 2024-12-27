from typing import Callable

import numpy as np


def read_full(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()


def read_lines(file_path: str) -> list[str]:
    with open(file_path, 'r') as f:
        return [line.rstrip() for line in f.readlines()]


def read_int_matrix(file_path: str, sep: str = ' ') -> np.ndarray:
    return np.array([*map(
        lambda line: [*map(int, line.split(sep) if sep else list(line))],
        read_lines(file_path),
    )])


def read_str_matrix(file_path: str) -> np.ndarray:
    return np.array([*map(
        lambda line: [*line],
        read_lines(file_path),
    )])

def str_to_str_matrix(s: str) -> np.ndarray:
    return np.array([*map(
        lambda line: [*line],
        s.split('\n'),
    )])

def int_array(s: str) -> np.ndarray:
    return np.array(
        [*map(int, s.split(' '))],
        dtype=np.int64,
    )


def split_once[T=str](s: str, sep: str, _map: Callable[[str], T] = None) -> tuple[T, T]:
    parts = s.split(sep, 1)

    if _map:
        parts = [*map(_map, parts)]

    return parts[0], parts[1]


def split_twice[T=str](s: str, sep: str, _map: Callable[[str], T] = None) -> tuple[T, T, T]:
    parts = s.split(sep, 2)

    if _map:
        parts = [*map(_map, parts)]

    return parts[0], parts[1], parts[2]