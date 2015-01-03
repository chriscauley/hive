import random
pieces = [
  "grasshopper", "grasshopper", "grasshopper",
  "ant", "ant", "ant",
  "fly", "fly", "fly",
  "wasp", "wasp", "wasp",
  "beetle", "beetle",
  "spider", "spider",
  "scorpion", "scorpion",
  "ladybug",
  "roach",
  "mosquito",
  "firefly",
  "pillbug",
  "centipede"
]
random.shuffle(pieces)
out = {}
for piece in pieces[:11]:
  out[piece] = out.get(piece,0)+1
for key,num in sorted(out.items()):
  print "%sx%s"%(num,key)
