#!/usr/bin/python3

from typing import List


def to_str(array: List[any], spacing: int=0) -> str:   
    space: str = " " * spacing
    return space.join(str(x) for x in array)


def to_str2D(array: List[List[any]], spacing: int=1) -> str:
    return "\n".join(to_str(list(arr), spacing) for arr in array)    


def add_char(array: List[any], char: str, count: int=1, interval: int=1, rng: list=[]) -> List[any]:
    char_sub: list = [char for _ in range(count)]
    max_range: int = int(len(array) / interval)
    rng_len: int = len(rng)

    if rng_len == 0:
        index = 0
        rng = range(0, max_range)
    elif rng_len == 1:
        rng = [rng[0]]
        index = rng[0]
        rng[0] = int(rng[0]/interval)
        rng = range(rng[0], max_range)
    else:
        rng = [rng[0], rng[1]]
        index = rng[0]
        rng[0], rng[1] = int(rng[0]/interval), int(rng[1]/interval)
        rng = range(rng[0], rng[1])

    for _ in rng:
        for _ in range(len(char_sub)):
            array.insert(index, char)
            index += 1

        index += interval

    return array


def add_char_in_2D(array: List[List[any]], char: str, count: int=1, interval: List[int]=[1, 1], in_rng: List[int]=[], out_rng: List[int]=[]) -> List[any]:
    out_interval = interval[1]
    in_interval = interval[0]

    if out_interval == 0:
        out_interval = 1
    if in_interval == 0:
        in_interval = 1

    max_out_range: int = int(len(array)/out_interval)
    out_rng_len: int = len(out_rng)

    if out_rng_len == 1:
        out_rng = range(out_rng[0], max_out_range)
    elif out_rng_len == 0:
        out_rng = range(0, max_out_range)
    else:
        out_rng[0], out_rng[1] = int(out_rng[0]/out_interval), int(out_rng[1]/out_interval)
        out_rng = range(out_rng[0], out_rng[1])

    index = out_rng[0]

    for _ in out_rng:
        array[index] = add_char(array[index], char, count, in_interval, in_rng)
        index += out_interval

    return array