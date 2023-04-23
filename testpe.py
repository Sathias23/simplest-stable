from decimal import Decimal
from enum import Enum
import random

def prompt_explorer_tag(prompt, tag, fragments, num_select):
  print(prompt)
  if tag in prompt:
    if num_select == 0:
      return prompt.replace(tag, "")
    else:
      split_fragments = fragments.split(", ")
      select_fragments = random.sample(split_fragments, k=num_select)
      replace = ", ".join(select_fragments)
      return prompt.replace(tag, replace)
  else:
    return prompt

def prompt_explorer(prompt: str, fragments: list, num_select: list):
  for i in range(len(fragments)):
    prompt = prompt_explorer_tag(prompt, f"<PE{i+1}>", fragments[i], num_select[i])
  return prompt

teststring = "<PE7>:1"
testtag = "<PE1>"
testfrag1 = " a distorted image of an abandoned mental asylum, a grainy video of a shadowy figure stalking through the woods, a glitchy photograph of a haunted doll, a cryptic message hidden within a corrupted file"
testnum1 = 1
testnum2 = 1
newstring = prompt_explorer_tag(teststring, testtag, testfrag1, testnum1)   
print(newstring)