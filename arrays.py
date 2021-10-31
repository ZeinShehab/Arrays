#!/usr/bin/python3

from typing import List


def to_str(array: List[any], spacing: int=0) -> str:   
    space: str = " " * spacing
    return space.join(str(x) for x in array)


def to_str3D(array: List[List[any]], spacing: int=1) -> str:
    return "\n".join(to_str(list(arr), spacing) for arr in array)    


def add_char(array: List[any], char: str, count: int=1, interval: int=1, rng: list=[False, False]) -> List[any]:
    char_sub: list = [char for _ in range(count)]

    if not rng[0] and not rng[1]:
        rng = range(0, int(len(array)/interval))
        index = 0
    else:
        index = rng[0]
        rng[0], rng[1] = int(rng[0]/interval), int(rng[1]/interval)
        rng = range(rng[0], rng[1])

    for _ in rng:
        for __ in range(len(char_sub)):
            array.insert(index, char)
            index += 1

        index += interval

    return array


def add_char_in_3D(array: List[List[any]], char: str, count: int=1, interval: List[int]=[1, 1], rng: List[List[int]]=[False, False]) -> List[any]:
    out_rng = rng[0]
    in_rng = rng[1]

    out_interval = interval[0]
    in_interval = interval[1]

    if interval[0] == 0:
        interval[0] == 1
    if interval[1] == 0:
        interval[1] == 1

    if not in_rng:
        in_rng = [False, False]

    if not out_rng:        
        out_rng = range(0, int(len(array)/out_interval))
        index = 0
    else:
        if out_rng[1] == "end":
            out_rng[1] = len(array)

        index = out_rng[0]
        out_rng[0], out_rng[1] = int(out_rng[0]/out_interval), int(out_rng[1]/out_interval)
        out_rng = range(out_rng[0], out_rng[1])

    for _ in out_rng:
        array[index] = add_char(array[index], char, count, in_interval, [in_rng[0], in_rng[1]])
        index += out_interval

    return array
