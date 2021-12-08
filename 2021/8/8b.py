from itertools import permutations

with open('small.txt') as f:
  lines = f.read().splitlines()

alphabet = 'abcdefg'
led_patterns = [
  'abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf',
  'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg'
]
inv_patterns = {v: k for k, v in enumerate(led_patterns)}

def translator(src, dst):
  mapping = dict(zip(src, dst))
  def translate(word):
    return inv_patterns[''.join(sorted(word.translate(word.maketrans(mapping))))]
  return translate

cnt = 0
for line in lines:
  probe, value = line.split(' | ')
  for perm in permutations(alphabet):
    t = translator(perm, alphabet)
    try:
      for word in probe.split(' '):
        t(word)
    except KeyError:
      continue
    break
  decoded = ''
  for word in value.split(' '):
    decoded += str(t(word))
  cnt += int(decoded)

print(cnt)
