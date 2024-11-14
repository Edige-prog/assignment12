from typing import List, Any, Dict, Set, Generator

def squares(n: int) -> List[int]:
    return [i * i for i in range(n)]

def unique_squares(numbers: List[int]) -> Set[int]:
    return {x * x for x in set(numbers)}

def char_counts(text: str) -> Dict[str, int]:
    return {char: text.count(char) for char in set(text)}

def flatten(nested_list: List[List[Any]]) -> List[Any]:
    return [item for sublist in nested_list for item in sublist]

def squares_gen(n: int) -> Generator[int, None, None]:
    return (i * i for i in range(n))

def odd_squares(n: int) -> set[int]:
    if n < 1:
        return set()
    return {x * x for x in range(1, n + 1) if x % 2 == 1}

def index_map(text: str) -> Dict[str, int]:
    return {char: idx for idx, char in enumerate(text)}

def unique_values(nested_list: List[List[Any]]) -> Set[Any]:
    return {item for sublist in nested_list for item in sublist}

def fibonacci_gen(n: int) -> Generator[int, None, None]:
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

def invert_dict(d: Dict[Any, Any]) -> Dict[Any, Any]:
    return {value: key for key, value in d.items()}

def primes(n: int) -> List[int]:
    return [
        x for x in range(2, n)
        if all(x % y != 0 for y in range(2, int(x ** 0.5) + 1))
    ]

def intersection(sets: List[Set[Any]]) -> Set[Any]:
    if not sets:
        return set()
    return {x for x in sets[0] if all(x in s for s in sets[1:])}

def factorials_gen(n: int) -> Generator[int, None, None]:
    from math import factorial
    gen_exp = (factorial(i) for i in range(n))
    for value in gen_exp:
        yield value


def str_lengths(strings: List[str]) -> Dict[str, int]:
    return {s: len(s) for s in strings}

def transpose(matrix: List[List[Any]]) -> List[List[Any]]:
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]

def reverse_gen(lst: List[Any]) -> Generator[Any, None, None]:
    return (lst[i] for i in range(len(lst) - 1, -1, -1))

def group_by_length(words: List[str]) -> Dict[int, List[str]]:
    return {
        length: [word for word in words if len(word) == length]
        for length in {len(word) for word in words}
    }

def common_elements(lists: List[List[Any]]) -> Set[Any]:
    if not lists:
        return set()
    return {x for x in lists[0] if all(x in lst for lst in lists[1:])}

def primes_gen(n: int) -> Generator[int, None, None]:
    for x in range(2, n + 1):
        if all(x % i != 0 for i in range(2, int(x ** 0.5) + 1)):
            yield x

def list_to_dict(lst: List[Any]) -> Dict[int, Any]:
    return {i: x for i, x in enumerate(lst)}
