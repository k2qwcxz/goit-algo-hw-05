import re 
from typing import Callable

def generator_numbers(text: str):
    patert = r'\s+(-?\d+\.?\d*)\s+'
    matches = re.finditer(patert, text)
    for match in matches:
        yield float(match)
def sum_profit(text: str, func: Callable) -> float:
    total = 0.0
    for number in func(text):
        total += number
    return total
