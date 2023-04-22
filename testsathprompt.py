from src.promptexplorer import PromptFragment, CombineMethod, Direction, PromptFragments
from src.synonymiser import Synonymiser

x = PromptFragments()
x.add_fragment("A cow, A bird, A camel", 1, 1)
x.add_fragment("by John, by Bill, by Jane, by Sarah, by Mary", 2, 0.5)
x.add_fragment("in the field, in the forest, in the desert", 1, 0.5)
x.add_fragment("with a hat, with a scarf, with a jacket", 1, -0.5)
pos = x.combine_fragments(CombineMethod.SELECT_NUM_DIRECTIONAL, Direction.POSITIVE)
neg = x.combine_fragments(CombineMethod.SELECT_NUM_DIRECTIONAL, Direction.NEGATIVE)

print(pos)
print(neg)
syn = Synonymiser(pos, 16)
prompt, distance = syn.synonymise()
print(f'Pos: {prompt} k:{distance}')
syn = Synonymiser(neg, 4)
prompt, distance = syn.synonymise()
print(f'Neg: {prompt} k:{distance}')

pos = "centered horrific detailed side view profile portrait of the angel of death, Día de los Muertos, red roses, skull makeup, stone wall background, ornamentation, thorns, vines, elegant"
neg = "lacklustre, repetitive, cropped, lowres, deformed, old, childish, cartoonish"
syn = Synonymiser(pos, 4)
prompt, distance = syn.synonymise()
print(f'Pos: {prompt} k:{distance}')
syn = Synonymiser(neg, 4)
prompt, distance = syn.synonymise()
print(f'Neg: {prompt} k:{distance}')

for i in range(1, 10):
    syn = Synonymiser(pos, i)
    prompt, distance = syn.synonymise()
    print(f'TopK: {i} Pos: {prompt} k:{distance}')