from . import instr
from . import tagloc

def resolve(loc: str, url: str) -> str:
    import requests 
    res = requests.get(url).text
    instrs = instr.from_string(loc)
    return tagloc.resolve(instrs, res)
