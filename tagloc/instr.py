from dataclasses import dataclass
from typing import List

@dataclass
class Instruction():
    pass

@dataclass
class VerticalMove(Instruction):
    n: int # 0: parent, n: nth-child

@dataclass
class HorizontalMove(Instruction):
    direction: int # 0: up-tree, 2: down-tree

@dataclass
class Search(Instruction):
    target: str # limit 1 for now

@dataclass
class Select(Instruction):
    target: str

@dataclass
class Attribute(Instruction):
    attr: str

def from_string(string: str) -> List[Instruction]:
    parts = string.split("::")

    def interpret_part(part: str) -> List[Instruction]:
        head = part[0]
        if len(part) > 1:
            tail = part[1:]
        if head == "$": # Search
            return [Search(tail)]
        elif head == ">":
            return [HorizontalMove(1) for i in range(int(tail))]
        elif head == "<":
            return [HorizontalMove(0) for i in range(int(tail))]
        elif head == "+":
            return [VerticalMove(int(tail))]
        elif head == "-":
            return [VerticalMove(0) for i in range(int(tail))]
        elif head == "%":
            return [Attribute(tail)]
        elif head == "~":
            return [Select(tail)]
        else:
            raise Exception("Invalid input: " + part)

    ls = []
    for part in parts:
        for instr in interpret_part(part):
            ls.append(instr)
    return ls
