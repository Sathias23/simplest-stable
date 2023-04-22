from decimal import Decimal
from enum import Enum
import random


class PromptFragment:
    def __init__(self, prompt: str, num_selections: int, weight: Decimal, variance: Decimal = 0):
        self.prompt = prompt
        self.weight = weight
        self.variance = variance
        self.num_selections = num_selections

    def as_is(self) -> str:
        return self.prompt

    def _select_num(self, weight_modifier=lambda x: x) -> str:
        split_prompt = self.prompt.split(", ")
        selected_prompt = random.sample(split_prompt, k=self.num_selections)
        return ", ".join([f"{s}:{weight_modifier(self.weight)}" for s in selected_prompt])

    def select_num(self) -> str:
        return self._select_num()

    def select_num_with_weight(self, direction: Enum) -> str:
        weight_modifier = lambda x: x if direction == Direction.POSITIVE else -x
        return self._select_num(weight_modifier)

    def select_num_with_rand_weight(self, direction: Enum) -> str:
        def weight_modifier(weight: Decimal) -> Decimal:
            rand_weight = round(random.uniform(weight - self.variance, weight + self.variance), 2)
            return rand_weight if direction == Direction.POSITIVE else -rand_weight

        return self._select_num(weight_modifier)


class CombineMethod(Enum):
    AS_IS = 0
    SELECT_NUM = 1
    SELECT_NUM_DIRECTIONAL = 2
    SELECT_NUM_WITH_WEIGHT = 3
    SELECT_NUM_WITH_RAND_WEIGHT = 4


class Direction(Enum):
    POSITIVE = 1
    NEGATIVE = 2


class PromptFragments:
    def __init__(self):
        self.fragments = []

    def clear(self):
        self.fragments.clear()

    def add_fragment(self, prompt: str, num_selections: int, weight: Decimal, variance: Decimal = 0):
        self.fragments.append(PromptFragment(prompt, num_selections, weight, variance))

    def combine_fragments(self, method: CombineMethod, direction: Direction = Direction.POSITIVE) -> str:
        if method == CombineMethod.AS_IS:
            return ", ".join([f.as_is() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM:
            return ", ".join([f.select_num() for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM_DIRECTIONAL:
            fragments = filter(lambda f: (f.weight > 0) == (direction == Direction.POSITIVE), self.fragments)
            return ", ".join([f.select_num() for f in fragments])
        elif method == CombineMethod.SELECT_NUM_WITH_WEIGHT:
            return " ".join([f.select_num_with_weight(direction) for f in self.fragments])
        elif method == CombineMethod.SELECT_NUM_WITH_RAND_WEIGHT:
            return " ".join([f.select_num_with_rand_weight(direction) for f in self.fragments])
        else:
            return "Error: Invalid combination of method and direction"
