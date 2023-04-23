from decimal import Decimal
from enum import Enum
import random

def prompt_explorer_tag(prompt, tag, fragments, num_select):
  print(prompt)
  if prompt.find(tag):
    if num_select == 0:
      return prompt.replace(tag, "")
    else:
      split_fragments = fragments.split(", ")
      select_fragments = random.sample(split_fragments, k=num_select)
      replace = ", ".join(select_fragments)
      return prompt.replace(tag, replace)

def prompt_explorer(prompt: str, fragments: list, num_select: list):
  for i in range(len(fragments)):
    prompt = prompt_explorer_tag(prompt, f"<PE{i+1}>", fragments[i], num_select[i])
  return prompt

teststring = "a <PE1> of a <PE2>"
testfrag1 = "picture, movie, sound"
testfrag2 = "cat, dog, bird"
testnum1 = 1
testnum2 = 1
newstring = prompt_explorer(teststring, [testfrag1, testfrag2], [testnum1, testnum2])
print(newstring)