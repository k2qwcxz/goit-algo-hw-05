import re 
from typing import Callable

def generator_numbers(text: str):
    pattern = r'\s+(-?\d+\.?\d*)\s+'
    matches = re.finditer(pattern, text)
    for match in matches:
        yield float(match.group()) 

def sum_profit(text: str, func: Callable) -> float:
    total = 0.0
    for number in func(text):
        total += number
    return total 

if __name__ == "__main__":
     text = "10 гномій йшло по лісу, 39 гномів вийшло з лісу й взяли з лісу 34 кілограми дров й 12 літрів води."

result = sum_profit(text, generator_numbers)
print(f"Сумма чисел в тексте: {result}")