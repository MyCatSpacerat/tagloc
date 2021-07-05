from typing import List
from . import instr

def resolve(instrs: List[instr.Instruction], content: str) -> str:
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(content, features="html.parser")
    cursor = soup

    def nth_child(soup: BeautifulSoup, n: int) -> BeautifulSoup:
        return list(soup.children)[n]

    for instruction in instrs:
        if isinstance(instruction, instr.Search):
            cursor = cursor.find(instruction.target)
        elif isinstance(instruction, instr.Attribute):
            cursor = cursor.attrs[instruction.attr]
        elif isinstance(instruction, instr.Select):
            cursor = cursor.select(instruction.target)
        elif isinstance(instruction, instr.HorizontalMove):
            if instruction.direction == 1:
                cursor = cursor.next_sibling
            elif instruction.direction == 0:
                cursor = cursor.previous_sibling
            else:
                raise Exception("Invalid direction: " + str(direction))
        elif isinstance(instruction, instr.VerticalMove):
            if instruction.n == 0:
                cursor = cursor.parent
            else:
                cursor = nth_child(cursor, instruction.n - 1)
    return cursor
